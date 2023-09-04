def proverb(input_list, *, qualifier="for want of"):
    """Generate the relevant proverb using the given list."""
    verses = []
    for index, item in enumerate(input_list[:-1], start=1):
        verses.append(f"For {qualifier} a {item}, the {input_list[index]} was lost.")
    verses.append(f"And all {qualifier} the {input_list[0]}.")
    return "\n".join(verses)