def recite(start_verse=1, end_verse=12):
    verses = {
        1: "This is the house that Jack built.",
        2: "This is the malt",
        3: "that lay in the house that Jack built.",
        4: "This is the rat",
        5: "that ate the malt",
        6: "that lay in the house that Jack built.",
        7: "This is the cat",
        8: "that killed the rat",
        9: "that ate the malt",
        10: "that lay in the house that Jack built.",
        11: "This is the farmer sowing his corn",
        12: "that the birds do eat."
    }

    result = []
    for i in range(start_verse, end_verse + 1):
        verse = verses[i]
        if i == start_verse:
            result.append("This is")
        else:
            result.append("This is the")

        if i % 2 != 0:
            result[-1] += f" {verse}"
        elif i > 1:
            result[-1] += f" that {verse}"

        if i < end_verse:
            result[-1] += ","
        result[-1] += "."

    return "\n".join(result)