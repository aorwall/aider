def recite(start, take=1):
    verses = []
    for verse in range(take):
        num_bottles = start - verse
        if num_bottles == 1:
            verses.append("One green bottle hanging on the wall,")
        elif num_bottles > 1:
            verses.append(f"{num_bottles} green bottles hanging on the wall,")
        else:
            verses.append("No more green bottles hanging on the wall!")
    return "\n".join(verses)
