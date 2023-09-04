def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse + 1):
        verse = "This is the"
        if i == start_verse:
            verse += f" {i}"
        else:
            verse += f" that {recite(start_verse, i - 1)}."
        verses.append(verse)
    return "\n\n".join(verses)
