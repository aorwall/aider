import itertools as it
import re
from itertools import permutations
from re import match

def solve(puzzle):
    # Remove spaces and convert to lowercase
    puzzle = puzzle.replace(' ', '').lower()

    # Get unique letters and sort them in descending order by their count
    letters = sorted(set(puzzle), key=lambda l: -puzzle.count(l))

    # Generate all possible combinations of digits for each letter
    digits = [range(0, 10) if l != 'e' else range(1, 10) for l in letters]

    for combination in it.product(*digits):   ## Fixed error here
        substitution = dict(zip(letters, map(str, combination)))

        try:
            left = eval(translate(puzzle.split('=')[0], substitution))
            right = eval(translate(puzzle.split('=')[1], substitution))

            if left == right:
                return {letter: int(digit) for letter, digit in zip(letters, combination)}

        except ZeroDivisionError:
            continue

    raise ValueError('No solution found')

def translate(expression, substitution):
    return ''.join([substitution[i] if i.isalpha() else i for i in expression])

if __name__ == "__main__":
    print(solve("send+more=money"))
