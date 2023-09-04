def proverb(input_list, *, qualifier=""):
    verses = []

    for idx, item in enumerate(input_list[:-1]):
        next_item = input_list[idx+1]

        if idx == len(input_list) - 2:
            verses.append(f"For want of a {item} the {next_item} was lost.")
        else:
            verses.append(f"For want of a {item} the {next_item} was lost.")

    verses.append(f"And all for the want of a {input_list[0]}{qualifier}.")

    return "\n".join(verses)