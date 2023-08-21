import re
from itertools import permutations

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle)
    unique_chars = set(''.join(words))
    assert len(unique_chars) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_chars = ''.join(first_letters) + ''.join(unique_chars - first_letters)
    characters = tuple(ord(c) for c in sorted_chars)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return {chr(c): str((g - ord('0'))) for c, g in zip(characters, guess)}
