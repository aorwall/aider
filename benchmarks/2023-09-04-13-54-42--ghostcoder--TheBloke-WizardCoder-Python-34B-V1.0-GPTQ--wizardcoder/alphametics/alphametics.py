import re
from itertools import permutations

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle)
    unique_letters = set(''.join(words))

    def get_number(word):
        perm = list(set(permutations([str(i) for i in range(1, 10)])))

        for p in perm:
            mapping = dict(zip(unique_letters, p))

            if ''.join([mapping[c] for c in word]) != '0':
                yield int(''.join([mapping[c] for c in word]))

    solutions = []

    for nums in zip(*map(get_number, words)):
        equation = puzzle.translate(str.maketrans({k: str(v) for k, v in zip(unique_letters, nums)}))
        try:
            left, right = map(int, equation.split())
        except ValueError:
            continue

        if left + right == int(equation.split()[-1]):
            solutions.append({k: int(v) for k, v in zip(unique_letters, nums)})

    return solutions or None
