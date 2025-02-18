def proverb(items, *, qualifier=None):
    if len(items) == 0:
        return ""

    verses = []
    for i in range(len(items)-1):
        verses.append("For want of a {} the {} was lost.".format(items[i], items[i+1]))

    qualifier_verse = "And all for the want of a {}{}".format(items[0], ".")
    if qualifier is not None:
        qualifier_verse += " " + str(qualifier)
    verses.append(qualifier_verse)

    return "\n".join(verses)