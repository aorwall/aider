def solve(puzzle):
    # Convert the puzzle into a dictionary
    puzzle_dict = {}
    for word in puzzle.split('+'):
        word = word.strip()
        for char in word:
            if char not in puzzle_dict:
                puzzle_dict[char] = 0
            puzzle_dict[char] += 1

    # Get the unique letters in the puzzle
    unique_letters = set(puzzle_dict.keys())

    # Initialize the solution with all letters set to 0
    solution = {letter: 0 for letter in unique_letters}

    # Iterate through the letters and try to solve the puzzle
    for letter in unique_letters:
        # Get the current letter count
        letter_count = puzzle_dict[letter]

        # Try to solve the puzzle for the current letter
        for i in range(10):
            # Check if the solution is valid
            if is_valid(solution, letter, i):
                # Update the solution
                solution[letter] = i
                break

    # Check if the solution is complete
    if len(solution) == len(unique_letters):
        return solution
    else:
        return None

def is_valid(solution, letter, value):
    # Check if the value is valid
    if value < 0 or value > 9:
        return False

    # Check if the letter is already used
    if letter in solution and solution[letter] != value:
        return False

    # Check if the sum is valid
    sum = 0
    for letter, value in solution.items():
        sum += value
    if sum != 10:
        return False

    return True
