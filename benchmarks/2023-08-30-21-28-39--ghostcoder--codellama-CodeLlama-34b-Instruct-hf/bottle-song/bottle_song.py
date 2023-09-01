def recite(start, take=1):
    if start < take:
        return []
    verses = []
    for i in range(start, start - take, -1):
        verses.append(verse(i))
    return verses

def verse(n):
    if n == 1:
        return "One green bottle hanging on the wall, one green bottle hanging on the wall, and if one green bottle should accidentally fall, there'll be no green bottles hanging on the wall."
    elif n == 2:
        return "Two green bottles hanging on the wall, two green bottles hanging on the wall, and if one green bottle should accidentally fall, there'll be one green bottle hanging on the wall."
    else:
        return f"{n} green bottles hanging on the wall, {n} green bottles hanging on the wall, and if one green bottle should accidentally fall, there'll be {n-1} green bottles hanging on the wall."
