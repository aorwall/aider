def solve(puzzle):
    # Convert the puzzle into a list of words
    words = puzzle.split()

    # Create a dictionary to map letters to digits
    letter_map = {}
    for word in words:
        for letter in word:
            if letter not in letter_map:
                letter_map[letter] = 0

    # Update the letter_map dictionary with the correct values for the letters in the puzzle
    for word in words:
        for letter in word:
            if letter not in letter_map:
                letter_map[letter] = 0

    # Iterate through the words and digits
    for i, word in enumerate(words):
        for j, letter in enumerate(word):
            # If the letter is already mapped, use the existing value
            if letter in letter_map:
                continue

            # If the letter is not mapped, try all possible values
            for value in range(10):
                # Check if the value is valid for the current position
                if value == 0 and j == 0:
                    continue
                if value > 0 and j == len(word) - 1:
                    continue

                # Check if the value is valid for the current word
                if word[0] == "0" and value == 0:
                    continue
                if word[-1] == "0" and value == 0:
                    continue

                # Check if the value is valid for the puzzle
                if i > 0 and words[i - 1][-1] == letter and value == 0:
                    continue
                if i < len(words) - 1 and words[i + 1][0] == letter and value == 0:
                    continue

                # If the value is valid, map the letter to the value
                letter_map[letter] = value
                break

    # Return the solved puzzle
    return "".join(str(letter_map[letter]) for letter in puzzle)
