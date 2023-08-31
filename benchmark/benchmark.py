#!/usr/bin/env python

import datetime
import json
import os
import random
import re
import shutil
import subprocess
import time
from abc import ABC, abstractmethod
from collections import defaultdict
from json.decoder import JSONDecodeError
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

import git
import lox
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceEndpoint, VertexAI

import prompts
import typer
from imgcat import imgcat
from rich.console import Console

from aider import models
from aider.coders import Coder
from aider.dump import dump  # noqa: F401
from aider.io import InputOutput
from ghostcoder.llm import LLMWrapper
from ghostcoder.schema import UpdatedFileItem

BENCHMARK_DNAME = Path(os.environ["AIDER_BENCHMARK_DIR"])

ORIGINAL_DNAME = BENCHMARK_DNAME / "exercism-python"

app = typer.Typer(add_completion=False, pretty_exceptions_enable=False)


def show_stats(dirnames):
    raw_rows = []
    for dirname in dirnames:
        row = summarize_results(dirname)
        raw_rows.append(row)

    return

    repeats = []
    seen = dict()
    rows = []
    for row in raw_rows:
        if not row:
            continue

        if row.model == "gpt-3.5-turbo":
            row.model = "gpt-3.5-turbo-0613"
        if row.edit_format == "diff-func-string":
            row.edit_format = "diff-func"

        if (
            row.model == "gpt-3.5-turbo-0613"
            and row.edit_format == "whole"
            and "repeat" not in row.dir_name
        ):
            # remember this row, so we can update it with the repeat_avg
            repeat_row = len(rows)

        pieces = row.model.split("-")
        row.model = "-".join(pieces[:3])
        if pieces[3:]:
            row.model += "\n-" + "-".join(pieces[3:])

        if row.completed_tests < 133:
            print(f"Warning: {row.dir_name} is incomplete: {row.completed_tests}")

        if "repeat" in row.dir_name:
            repeats.append(vars(row))
            continue

        kind = (row.model, row.edit_format)
        if kind in seen:
            dump(row.dir_name)
            dump(seen[kind])
            return

        seen[kind] = row.dir_name
        rows.append(vars(row))

    if repeats:
        extra = rows[repeat_row]
        dump(extra)
        repeats.append(extra)
        repeats = pd.DataFrame.from_records(repeats)
        repeat_max = repeats["pass_rate_2"].max()
        repeat_min = repeats["pass_rate_2"].min()
        repeat_avg = repeats["pass_rate_2"].mean()

        repeat_lo = repeat_avg - repeat_min
        repeat_hi = repeat_max - repeat_avg

        dump(repeat_max)
        dump(repeat_min)
        dump(repeat_avg)

        # use the average in the main bar
        rows[repeat_row]["pass_rate_2"] = repeat_avg

    df = pd.DataFrame.from_records(rows)
    df.sort_values(by=["model", "edit_format"], inplace=True)

    tries = [df.groupby(["model", "edit_format"])["pass_rate_2"].mean()]
    if True:
        tries += [df.groupby(["model", "edit_format"])["pass_rate_1"].mean()]

    plt.rcParams["hatch.linewidth"] = 0.5
    plt.rcParams["hatch.color"] = "#444444"

    from matplotlib import rc

    rc("font", **{"family": "sans-serif", "sans-serif": ["Helvetica"], "size": 10})

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.grid(axis="y", zorder=0, lw=0.2)

    zorder = 1
    for grouped in tries:
        zorder += 1
        df = grouped.unstack()
        num_models, num_formats = df.shape

        pos = np.array(range(num_models))
        width = 0.8 / num_formats

        formats = df.columns
        models = df.index

        for i, fmt in enumerate(formats):
            if zorder > 1:
                edge = dict(
                    edgecolor="#ffffff",
                    linewidth=1.5,
                )
            else:
                edge = dict()
            if zorder == 2:
                edge["label"] = fmt

            color = "#b3e6a8" if "diff" in fmt else "#b3d1e6"
            hatch = "////" if "func" in fmt else ""
            rects = ax.bar(
                pos + i * width,
                df[fmt],
                width * 0.95,
                color=color,
                hatch=hatch,
                zorder=zorder,
                **edge,
            )
            if zorder == 2:
                ax.bar_label(rects, padding=4, labels=[f"{v:.0f}%" for v in df[fmt]], size=6)

    if len(repeats):
        ax.errorbar(
            1.4,
            repeat_avg,
            yerr=[[repeat_lo], [repeat_hi]],
            fmt="none",
            zorder=5,
            capsize=2.5,
            elinewidth=1,
            markeredgewidth=1,
        )

    ax.set_xticks([p + 1.5 * width for p in pos])
    ax.set_xticklabels(models)

    top = 95
    ax.annotate(
        "First attempt,\nbased on\ninstructions",
        xy=(2.9, 51),
        xytext=(2.5, top),
        horizontalalignment="center",
        verticalalignment="top",
        arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=0.3"},
    )
    ax.annotate(
        "Second attempt,\nbased on\nunit test errors",
        xy=(3.1, 68),
        xytext=(4.25, top),
        horizontalalignment="center",
        verticalalignment="top",
        arrowprops={"arrowstyle": "->", "connectionstyle": "arc3,rad=0.3"},
    )

    ax.set_ylabel("Percent of exercises completed successfully")
    # ax.set_xlabel("Model")
    ax.set_title("GPT Code Editing")
    ax.legend(
        title="Edit Format",
        loc="upper left",
        # bbox_to_anchor=(0.95, 0.95),
    )
    ax.set_ylim(top=100)

    plt.tight_layout()
    plt.savefig("tmp.svg")
    imgcat(fig)

    # df.to_csv("tmp.benchmarks.csv")


def resolve_dirname(dirname, use_single_prior, make_new, agent, model, edit_format):
    if len(dirname.parts) > 1:
        return dirname

    priors = list(BENCHMARK_DNAME.glob(f"*--{dirname}"))
    if len(priors) == 1 and use_single_prior:
        dirname = priors[0].name
        print(f"Using pre-existing {dirname}")
    elif len(priors):
        if not make_new:
            print(f"Prior runs of {dirname} exist, use --new or name one explicitly")
            print()
            for prior in priors:
                print(prior)
            return

    if not re.match(r"\d\d\d\d-\d\d-\d\d-", str(dirname)):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d-%H-%M-%S--")
        dirname = now + agent + "--" + model.replace("/", "-")
        if edit_format:
            dirname += "--" + edit_format

    dirname = BENCHMARK_DNAME / dirname
    return dirname


@app.command()
def main(
    dirnames: List[str] = typer.Argument(..., help="Directory names"),
    agent: str = typer.Option("aider", "--agent", "-a", help="Agent name"),
    provider: str = typer.Option("openai", "--provider", "-p", help="LLM runtime provider name"),
    model: str = typer.Option("gpt-3.5-turbo", "--model", "-m", help="Model name"),
    edit_format: str = typer.Option(None, "--edit-format", "-e", help="Edit format"),
    keywords: str = typer.Option(
        None, "--keywords", "-k", help="Only run tests that contain keywords (comma sep)"
    ),
    clean: bool = typer.Option(
        False, "--clean", "-c", help="Discard the existing testdir and make a clean copy"
    ),
    cont: bool = typer.Option(False, "--cont", help="Continue the (single) matching testdir"),
    make_new: bool = typer.Option(False, "--new", "-n", help="Make a new dated testdir"),
    no_unit_tests: bool = typer.Option(False, "--no-unit-tests", help="Do not run unit tests"),
    no_aider: bool = typer.Option(False, "--no-aider", help="Do not run aider"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
    stats_only: bool = typer.Option(
        False, "--stats", "-s", help="Do not run tests, just collect stats on completed tests"
    ),
    diffs_only: bool = typer.Option(False, "--diffs", help="Just diff the provided stats dirs"),
    tries: int = typer.Option(2, "--tries", "-r", help="Number of tries for running tests"),
    threads: int = typer.Option(1, "--threads", "-t", help="Number of threads to run in parallel"),
    num_tests: int = typer.Option(-1, "--num-tests", "-n", help="Number of tests to run"),
):
    repo = git.Repo(search_parent_directories=True)
    commit_hash = repo.head.object.hexsha[:7]
    if repo.is_dirty():
        commit_hash += "-dirty"

    if len(dirnames) > 1 and not (stats_only or diffs_only):
        print("Only provide 1 dirname unless running with --stats or --diffs")
        return 1

    if agent not in ["aider", "ghostcoder"]:
        print("Unknown agent, must be one of: aider, ghostcoder")
        return 1

    updated_dirnames = []
    for dirname in dirnames:
        dirname = Path(dirname)
        dirname = resolve_dirname(dirname, stats_only or cont, make_new, agent, model, edit_format)
        if not dirname:
            return 1
        updated_dirnames.append(dirname)

    if stats_only:
        return show_stats(updated_dirnames)

    if diffs_only:
        return show_diffs(updated_dirnames)

    assert len(updated_dirnames) == 1, updated_dirnames
    dirname = updated_dirnames[0]

    if "AIDER_DOCKER" not in os.environ:
        print("Warning: benchmarking runs unvetted code from GPT, run in a docker container")
        return

    assert BENCHMARK_DNAME.exists() and BENCHMARK_DNAME.is_dir(), BENCHMARK_DNAME
    assert ORIGINAL_DNAME.exists() and ORIGINAL_DNAME.is_dir(), ORIGINAL_DNAME

    if clean and dirname.exists():
        print("Cleaning up and replacing", dirname)
        dir_files = set(fn.name for fn in dirname.glob("*"))
        original_files = set(fn.name for fn in ORIGINAL_DNAME.glob("*"))
        if dir_files != original_files:
            print("ERROR: will not delete dir that does not look like original tests", dirname)
            return

        dest = dirname.parent / "OLD" / dirname.name
        if dest.exists():
            old_now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            dest = dirname.parent / "OLD" / (old_now + dirname.name)

        dirname.rename(dest)

    if not dirname.exists():
        shutil.copytree(ORIGINAL_DNAME, dirname)

    test_dnames = sorted(os.listdir(dirname))

    if keywords:
        keywords = keywords.split(",")
        test_dnames = [dn for dn in test_dnames for keyword in keywords if keyword in dn]

    random.shuffle(test_dnames)
    if num_tests > 0:
        test_dnames = test_dnames[:num_tests]

    if threads == 1:
        all_results = []
        for testname in test_dnames:
            results = run_test(
                dirname / testname,
                agent,
                model,
                provider,
                edit_format,
                tries,
                no_unit_tests,
                no_aider,
                verbose,
                commit_hash,
            )

            all_results.append(results)
            summarize_results(dirname)
    else:
        run_test_threaded = lox.thread(threads)(run_test)
        for testname in test_dnames:
            run_test_threaded.scatter(
                dirname / testname,
                model,
                edit_format,
                tries,
                no_unit_tests,
                no_aider,
                verbose,
                commit_hash,
            )
        all_results = run_test_threaded.gather(tqdm=True)

    print()
    print()
    print()
    summarize_results(dirname)

    return 0


def show_diffs(dirnames):
    dirnames = sorted(dirnames)

    all_results = dict((dirname, load_results(dirname)) for dirname in dirnames)
    testcases = set()
    for results in all_results.values():
        testcases.update(result["testcase"] for result in results)

    testcases = sorted(testcases)

    unchanged = set()

    for testcase in testcases:
        all_outcomes = []
        for dirname in dirnames:
            results = all_results[dirname]
            result = [r for r in results if r["testcase"] == testcase][0]

            outcomes = tuple(result["tests_outcomes"])
            all_outcomes.append(True in outcomes)

        if len(set(all_outcomes)) == 1:
            unchanged.add(testcase)
            continue

        print()
        print(testcase)
        for outcome, dirname in zip(all_outcomes, dirnames):
            print(outcome, f"{dirname}/{testcase}/.aider.chat.history.md")

    changed = set(testcases) - unchanged
    print()
    print("changed:", len(changed), ",".join(sorted(changed)))
    print("unchanged:", len(unchanged), ",".join(sorted(unchanged)))


def load_results(dirname):
    dirname = Path(dirname)
    all_results = [json.loads(fname.read_text()) for fname in dirname.glob("*/.aider.results.json")]
    return all_results


def summarize_results(dirname):
    all_results = load_results(dirname)

    res = SimpleNamespace()
    res.total_tests = len(list(Path(dirname).glob("*")))

    try:
        tries = max(len(results["tests_outcomes"]) for results in all_results if results)
    except ValueError:
        tries = 0

    res.dir_name = str(dirname)

    test_reports = ["testcase,model,edit format,passed tests,error outputs,cost,duration"]

    passed_tests = [0] * tries

    res.completed_tests = 0
    res.duration = 0
    res.cost = 0
    res.error_outputs = 0
    res.user_asks = 0
    res.test_timeouts = 0
    res.exhausted_context_windows = 0

    variants = defaultdict(set)

    for results in all_results:
        if not results:
            continue

        res.completed_tests += 1
        passed = results["tests_outcomes"][-1]
        if passed:
            for i in range(len(results["tests_outcomes"]) - 1, tries):
                passed_tests[i] += 1

        res.cost += results["cost"]
        res.duration += results["duration"]
        res.test_timeouts += results.get("test_timeouts", 0)

        res.error_outputs += results.get("num_error_outputs", 0)
        res.user_asks += results.get("num_user_asks", 0)
        res.exhausted_context_windows += results.get("num_exhausted_context_windows", 0)

        test_reports.append(f"{results['testcase']},{results['model']},{results['edit_format']},{passed},"
                            f"{results.get('num_error_outputs')},{results['cost']},{results['duration']}")

        for key in "agent model edit_format commit_hash".split():
            val = results.get(key)
            variants[key].add(val)

    if not res.completed_tests:
        return

    tname = dirname / ".report.csv"
    tname.write_text("\n".join(test_reports))

    console = Console(highlight=False)
    console.rule(title=str(dirname))

    console.print(f"test-cases: {res.completed_tests}")
    for key, val in variants.items():
        if len(val) > 1:
            style = "red"
        else:
            style = None
        val = ", ".join(map(str, val))
        setattr(res, key, val)
        console.print(f"{key}: {val}", style=style)
    print("num_error_outputs:", res.error_outputs)
    print("num_user_asks:", res.user_asks)

    style = "red" if res.exhausted_context_windows else None
    console.print("num_exhausted_context_windows", res.exhausted_context_windows, style=style)

    style = "red" if res.test_timeouts else None
    console.print("test_timeouts:", res.test_timeouts, style=style)

    console.print()
    for i in range(tries):
        pass_rate = 100 * passed_tests[i] / res.completed_tests
        console.print(f"{pass_rate:.1f}% correct after try {i}")
        setattr(res, f"pass_rate_{i+1}", pass_rate)

    console.print()
    res.avg_duration = res.duration / res.completed_tests

    console.print(f"duration: {res.avg_duration:.1f} sec/test-case")

    res.avg_cost = res.cost / res.completed_tests

    projected_cost = res.avg_cost * res.total_tests

    console.print(
        f"costs: ${res.avg_cost:.4f}/test-case, ${res.cost:.2f} total,"
        f" ${projected_cost:.2f} projected"
    )

    console.rule()

    # print(json.dumps(vars(res), indent=4, sort_keys=True))
    return res


def run_test(
    testdir, agent_name, model_name, provider, edit_format, tries, no_unit_tests, no_aider, verbose, commit_hash
):
    if not os.path.isdir(testdir):
        print("Not a dir:", testdir)
        return

    testdir = Path(testdir)

    results_fname = testdir / ".aider.results.json"
    if results_fname.exists():
        try:
            res = json.loads(results_fname.read_text())
            return res
        except JSONDecodeError:
            print(f"{results_fname} failed to parse, skipping")
            return

    fnames = []
    for fname in testdir.glob("*"):
        if "test" not in fname.name and fname.is_file() and fname.name[0] != ".":
            fnames.append(fname)

            # restore the original file, in case we interrupted a prev run
            # after it had saved changes
            original_fname = ORIGINAL_DNAME / testdir.name / fname.name
            shutil.copy(original_fname, fname)

    file_list = " ".join(fname.name for fname in fnames)

    instructions = ""

    introduction = testdir / ".docs/introduction.md"
    if introduction.exists():
        instructions += introduction.read_text()
    instructions += (testdir / ".docs/instructions.md").read_text()
    instructions_append = testdir / ".docs/instructions.append.md"
    if instructions_append.exists():
        instructions += instructions_append.read_text()

    instructions += prompts.instructions_addendum.format(file_list=file_list)

    show_fnames = ",".join(map(str, fnames))
    print("fnames:", show_fnames)

    if agent_name == "aider":
        agent: CodeAgent = AiderAgent(
            testdir=testdir,
            model_name=model_name,
            edit_format=edit_format,
            fnames=fnames,
            verbose=verbose
        )
    elif agent_name == "ghostcoder":
        agent: CodeAgent = GhostCoderAgent(
            testdir=testdir,
            model_name=model_name,
            edit_format=edit_format,
            provider=provider,
            fnames=fnames,
            verbose=verbose
        )

    timeouts = 0

    dur = 0
    test_outcomes = []
    for i in range(tries):
        start = time.time()
        if not no_aider:
            agent.run(with_message=instructions)
        dur += time.time() - start

        if no_unit_tests:
            break

        try:
            errors = run_unit_tests(testdir)
        except subprocess.TimeoutExpired:
            errors = "Tests timed out!"
            timeouts += 1

        if errors:
            test_outcomes.append(False)
        else:
            test_outcomes.append(True)
            break

        errors = errors.splitlines()
        print(errors[-1])
        errors = errors[:50]
        errors = "\n".join(errors)
        instructions = errors
        instructions += prompts.test_failures.format(file_list=file_list)

    results = dict(
        testdir=str(testdir),
        testcase=testdir.name,
        agent=agent_name,
        model=model_name,
        edit_format=edit_format,
        tests_outcomes=test_outcomes,
        cost=agent.total_cost,
        duration=dur,
        test_timeouts=timeouts,
        commit_hash=commit_hash,
        num_error_outputs=agent.num_error_outputs,
        num_user_asks=agent.num_user_asks,
        num_exhausted_context_windows=agent.num_exhausted_context_windows,
        chat_hashes=list(
            zip(
                agent.chat_completion_call_hashes,
                agent.chat_completion_response_hashes,
            )
        ),
    )
    dump(results)

    results_fname.write_text(json.dumps(results, indent=4))

    return results


def run_unit_tests(testdir):
    command = [
        "python",
        "-m",
        "unittest",
        "discover",
        "-s",
        str(testdir),
        "-t",
        str(testdir),
        "-p",
        "*_test.py",
    ]
    print(" ".join(command))

    timeout = 60

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        timeout=timeout,
    )

    success = result.returncode == 0
    res = result.stdout
    res = cleanup_test_output(res, testdir)

    if not success:
        print(f"Tests failed: {testdir}")
        return res


def cleanup_test_output(output, testdir):
    # remove timing info, to avoid randomizing the response to GPT
    res = re.sub(
        r"^Ran \d+ tests in \d+\.\d+s$",
        "",
        output,
        flags=re.MULTILINE,
    )
    res = re.sub(
        r"^====*$",
        "====",
        res,
        flags=re.MULTILINE,
    )
    res = re.sub(
        r"^----*$",
        "----",
        res,
        flags=re.MULTILINE,
    )

    res = res.replace(str(testdir), str(testdir.name))
    return res


class CodeAgent(ABC):

    @abstractmethod
    def run(self, with_message: str) -> None:
        pass

    @abstractmethod
    def total_cost(self) -> float:
        pass

    @abstractmethod
    def num_error_outputs(self) -> int:
        pass

    @abstractmethod
    def num_user_asks(self) -> int:
        pass

    @abstractmethod
    def num_exhausted_context_windows(self) -> int:
        pass

    @abstractmethod
    def chat_completion_call_hashes(self) -> List[str]:
        pass

    @abstractmethod
    def chat_completion_response_hashes(self) -> List[str]:
        pass


class AiderAgent(CodeAgent):

    def __init__(self, testdir: Path, model_name: str, edit_format: str, fnames: List[Path], verbose: bool):
        self.history_fname = testdir / ".aider.chat.history.md"

        self.io = InputOutput(
            pretty=True,
            yes=False,
            chat_history_file=self.history_fname,
        )

        main_model = models.Model(model_name)
        edit_format = edit_format or main_model.edit_format

        dump(main_model)
        dump(edit_format)

        self.coder = Coder.create(
            main_model,
            edit_format,
            self.io,
            fnames=fnames,
            use_git=False,
            stream=False,
            pretty=False,
            verbose=verbose,
        )

    def run(self, with_message: str):
        self.coder.run(with_message=with_message)

        if self.coder.last_keyboard_interrupt:
            raise KeyboardInterrupt

    @property
    def total_cost(self):
        return self.coder.total_cost

    @property
    def num_error_outputs(self):
        return self.io.num_error_outputs

    @property
    def num_user_asks(self):
        return self.io.num_user_asks

    @property
    def num_exhausted_context_windows(self):
        return self.coder.num_exhausted_context_windows

    @property
    def chat_completion_call_hashes(self):
        return self.coder.chat_completion_call_hashes

    @property
    def chat_completion_response_hashes(self):
        return self.coder.chat_completion_response_hashes


_ghostcoder_llm = None


class GhostCoderAgent(CodeAgent):

    def __init__(self, testdir: Path, model_name: str, edit_format: str, provider: str, fnames: List[Path], verbose: bool):
        from ghostcoder import FileRepository
        from ghostcoder.callback import LogCallbackHandler
        from ghostcoder.actions import WriteCodeAction
        from ghostcoder.llm import LLMWrapper, ChatLLMWrapper
        from ghostcoder.llm.alpaca import AlpacaLLMWrapper

        callback = LogCallbackHandler(str(testdir / "prompt_log"))

        import logging
        logging.basicConfig(level=logging.INFO)

        global _ghostcoder_llm
        if not _ghostcoder_llm:
            if provider == "vertex-ai":
                _ghostcoder_llm = LLMWrapper(llm=VertexAI(
                    model_name=model_name,
                    project="albert-test-368916", # TODO: Configure this
                    max_output_tokens=2048,
                    temperature=0.0,
                    callbacks=[callback]
                ))
            elif provider == "huggingface":
                import torch
                from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
                from langchain.llms import HuggingFacePipeline

                model = AutoModelForCausalLM.from_pretrained(model_name,
                                                             torch_dtype=torch.float16,
                                                             device_map="auto",
                                                             revision="main")

                tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
                pipe = pipeline(
                    "text-generation",
                    model=model,
                    tokenizer=tokenizer,
                    max_new_tokens=1024,
                    temperature=0.01,
                )
                # TODO: Configure this
                _ghostcoder_llm = AlpacaLLMWrapper(
                    HuggingFacePipeline(pipeline=pipe,
                                        callbacks=[callback],
                                        verbose=True))
            else:
                _ghostcoder_llm = ChatLLMWrapper(ChatOpenAI(
                    model=model_name,
                    temperature=0,
                    callbacks=[callback]
                ))

        repository = FileRepository(repo_path=str(testdir), use_git=False)
        self.action = WriteCodeAction(
            llm=_ghostcoder_llm,
            repository=repository,
            sys_prompt_id=edit_format
        )
        self.chat_history_fname = testdir / ".chat.history.json"
        self.fnames = fnames
        self.message_history = []
        self._total_cost = 0
        self._num_error_outputs = 0

    def run(self, with_message: str):
        from ghostcoder.schema import FileItem, TextItem, Message

        items = []
        items.extend([FileItem(file_path=str(fname.name), language="pyton") for fname in self.fnames])
        items.append(TextItem(text=with_message))

        human_msg = Message(sender="Human", items=items)
        ai_messages = self.action.execute(message=human_msg, message_history=self.message_history)

        self.message_history.append(human_msg)
        self.message_history.extend(ai_messages)
        for message in self.message_history:
            message.items = [item for item in message.items
                             if not isinstance(item, FileItem) and not isinstance(item, UpdatedFileItem)]
        self._save_message(self.chat_history_fname, self.message_history)

        stats = [msg.stats for msg in ai_messages if msg.stats]
        if stats:
            total_usage = sum(stats[1:], stats[0])
            self._total_cost += total_usage.total_cost

        if len(ai_messages[-1].find_items_by_type("updated_file")) == 0:
            print("Missing updated_file in ai_message")
            self._num_error_outputs += 1

        if ai_messages[-1].stats and ai_messages[-1].stats.metrics:
            if ai_messages[-1].stats.metrics.get("hallucinated_file", 0) > 0:
                print("Hallucinated file in ai_message")
                self._num_error_outputs += 1

            if ai_messages[-1].stats.metrics.get("no_change", 0) > 0:
                print("No change in updated file")
                self._num_error_outputs += 1

    def _save_message(self, cfile: Path, messages):
        dicts = [msg.dict() for msg in messages]
        with open(cfile, "w") as file:
            json.dump(dicts, file, indent=2)


    @property
    def total_cost(self):
        return self._total_cost

    @property
    def num_error_outputs(self):
        return self._num_error_outputs

    @property
    def num_user_asks(self):
        return 0

    @property
    def num_exhausted_context_windows(self):
        return 0

    @property
    def chat_completion_call_hashes(self):
        return ""

    @property
    def chat_completion_response_hashes(self):
        return ""


if __name__ == "__main__":
    app()
