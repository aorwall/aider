import os
os.environ['AIDER_BENCHMARK_DIR'] = '/home/albert/repos/albert/aider/benchmarks'
os.environ['AIDER_DOCKER'] = 'true'
os.chdir("/home/albert/repos/albert/aider")

import benchmark
#from typer.testing import CliRunner

#runner = CliRunner()
#result = runner.invoke(app, ["benchmarks", "--agent", "ghostcoder", "--model", "TheBloke/Phind-CodeLlama-34B-v2-GPTQ", "--edit-format", "default", "--new"])
#print(result.stdout)



print(benchmark.main(
    dirnames=["benchmarks"],
    agent="ghostcoder",
    provider="exllama",
    model="TheBloke/Phind-CodeLlama-34B-v2-GPTQ",
    edit_format="default",
    keywords=None,
    make_new=True,
    clean= False,
    cont = False,
    no_unit_tests = False,
    no_aider = False,
    verbose = False,
    stats_only = False,
    diffs_only = False,
    tries = 2,
    threads = 1,
    num_tests = 1
))

