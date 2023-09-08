def recite(start_verse, end_verse):
    verses = []
    for day in range(start_verse, end_verse + 1):
        verses.append(get_verse(day))
    return verses
