import re
from itertools import permutations

def solve(puzzle):
    # Extract the words from the puzzle
    words = re.findall('[A-Z]+', puzzle)

    # Get the unique letters in the puzzle
    letters = set(''.join(words))

    # Create a list of possible digits for each letter
    digits = [list(range(10))] * len(letters)

    # Generate all possible combinations of digits for the letters
    possibilities = permutations(*digits)

    # Iterate over the possibilities and check if they satisfy the equation
    for possibility in possibilities:
        substitution = dict(zip(letters, map(str, possibility)))

        # Check if the equation is satisfied
        left = eval(f"{'+'.join(map(lambda x: substitution[x], words[0]))}")
        right = eval(f"{'+'.join(map(lambda x: substitution[x], words[1]))}")
        if left + right == eval(f"{'+'.join(map(lambda x: substitution[x], words[2]))}"):
            return ' '.join(word.translate(str.maketrans(substitution)) for word in words)

    # If no solution was found, return None
    return None
