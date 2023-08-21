from itertools import permutations

def solve(puzzle):
    # Extract the words and result from the puzzle
    words = puzzle.split()
    result = words[-1]
    words = words[:-2]

    # Get all unique letters from the puzzle
    letters = set(''.join(words + [result]))

    # Generate all possible permutations of digits for the letters
    digits = range(10)
    for permutation in permutations(digits, len(letters)):
        # Create a mapping of letters to digits
        mapping = dict(zip(letters, permutation))

        # Replace the letters with digits in the puzzle
        replaced_words = [word.translate(str.maketrans(mapping)) for word in words]
        replaced_result = result.translate(str.maketrans(mapping))

        # Check if the replaced puzzle is valid
        if all(word[0] != '0' for word in replaced_words) and int(replaced_words[-1]) == sum(int(word) for word in replaced_words[:-1]):
            return mapping

    return None
