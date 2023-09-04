def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = get_verse(i + 1)
        verses.append(verse)
    return "\n".join(verses)


def get_verse(verse_number):
    if verse_number == 1:
        return "I know an old man who swallowed a fly."
    elif verse_number == 2:
        return "I don't know why he swallowed the fly. Perhaps he'll die."
    else:
        raise ValueError("Invalid verse number")


if __name__ == "__main__":
    print(recite(1, 2))
