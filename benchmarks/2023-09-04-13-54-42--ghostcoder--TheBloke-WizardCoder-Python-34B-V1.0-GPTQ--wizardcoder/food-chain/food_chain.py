def recite(start_verse=1, end_verse=8):
    verses = []

    for i in range(start_verse, end_verse + 1):
        verse = f"I know an old lady who swallowed a {foods[i - 1]}."

        if i == 1:
            verse += "\n"
        else:
            verse += f" She swallowed the {foods[i - 2]} to catch the {foods[i - 1]}.\n"

        verses.append(verse)

    return verses


foods = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]