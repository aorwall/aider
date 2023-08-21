def recite(start_verse, end_verse):
    animals = [
        ("fly", ""),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = ["I know an old lady who swallowed a {}.".format(animals[i][0])]
        if animals[i][1]:
            verse.append(animals[i][1])
        if i != len(animals) - 1:
            for j in range(i, -1, -1):
                if j == 0:
                    verse.append("She swallowed the {} to catch the {}.".format(animals[j+1][0], animals[j][0]))
                else:
                    if animals[j][0] == "spider":
                        verse.append("She swallowed the {} to catch the {} that {}.".format(animals[j+1][0], animals[j][0], animals[j][1].lower()))
                    else:
                        verse.append("She swallowed the {} to catch the {}.".format(animals[j+1][0], animals[j][0]))
            verse.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        verses.append("\n".join(verse))

    return verses