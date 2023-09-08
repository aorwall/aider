def solve(puzzle):
    """
    Solve an alphametic puzzle.

    Args:
        puzzle (str): The puzzle to solve.

    Returns:
        dict: A dictionary of the solution with letters as keys and numbers as values.
    """
    from collections import defaultdict
    from itertools import permutations

    # Remove spaces and newlines from the puzzle
    puzzle = puzzle.replace(" ", "").replace("\n", "")

    # Find all the words in the puzzle
    words = puzzle.split("+")

    # Create a set of unique letters in the puzzle
    letters = set("".join(words))

    # Create a list of possible digits for each letter
    possible_digits = defaultdict(list)
    for letter in letters:
        for digit in range(1, 10):
            if letter not in possible_digits or digit not in possible_digits[letter]:
                possible_digits[letter].append(digit)

    # Filter out invalid permutations of digits
    for word in words:
        for perm in permutations(possible_digits[word[0]], len(word)):
            if int("".join(str(d) for d in perm)) % 10 != 0:
                possible_digits[word[0]] = [int("".join(str(d) for d in perm))]

    # Solve the puzzle
    for perm in permutations(range(1, 10), len(letters)):
        solution = dict(zip(letters, perm))
        if all(sum(solution[letter] for letter in word) % 10 == 0 for word in words):
            return solution

    # No solution found
    return None
