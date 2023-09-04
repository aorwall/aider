def score(word):
    scores = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'l': 1, 'r': 1, 's': 1, 'u': 1, 't': 1, 'd': 2, 'g': 2, 'b': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}
    total = 0
    for char in word:
        try:
            total += scores[char.lower()]
        except KeyError:
            pass
        if char.isupper():
            total += 7
    return total
