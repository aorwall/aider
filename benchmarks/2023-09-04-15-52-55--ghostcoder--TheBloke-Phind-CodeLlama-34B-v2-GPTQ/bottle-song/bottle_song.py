def verse(num):
    if num == 0:
        return "No more bottles hanging on the wall,"
    elif num == 1:
        return "1 green bottle hanging on the wall,"
    else:
        return f"{num} green bottles hanging on the wall,"

def recite(start, take=1):
    verses = []
    for i in range(take):
        n = start - i
        verses.append(f"{verse(n)}\n{verse(n)} on the wall.\n")

    return "".join(verses)
