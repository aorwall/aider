def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        verses.append(_verse(i))
    return verses

def _verse(num_bottles):
    if num_bottles == 1:
        return "One green bottle hanging on the wall,\nOne green bottle hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be no green bottles hanging on the wall."
    else:
        return f"{num_bottles} green bottles hanging on the wall,\n{num_bottles} green bottles hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {num_bottles - 1} green bottles hanging on the wall."

# Test the function
print(recite(10))
