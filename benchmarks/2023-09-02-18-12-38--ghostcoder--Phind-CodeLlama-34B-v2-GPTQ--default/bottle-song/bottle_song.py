def recite(start=10, take=1):
    verses = [
        "Ten green bottles hanging on the wall,",
        "Nine green bottles hanging on the wall,",
        "Eight green bottles hanging on the wall,",
        "Seven green bottles hanging on the wall,",
        "Six green bottles hanging on the wall,",
        "Five green bottles hanging on the wall,",
        "Four green bottles hanging on the wall,",
        "Three green bottles hanging on the wall,",
        "Two green bottles hanging on the wall,",
        "One green bottle hanging on the wall,"
    ]

    result = []
    for i in range(start-1, start-take-1, -1):
        verse = f"{verses[i]} {verses[i]}" if i > 0 else f"No more green bottles hanging on the wall!"
        result.append(verse)

    return "\n".join(result)