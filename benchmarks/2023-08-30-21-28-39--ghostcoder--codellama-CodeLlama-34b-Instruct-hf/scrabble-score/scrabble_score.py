def score(word):
    # Initialize the score to 0
    score = 0

    # Iterate through each letter in the word
    for letter in word:
        # Check if the letter is in the dictionary
        if letter in letter_values:
            # Add the value of the letter to the score
            score += letter_values[letter]
        else:
            # If the letter is not in the dictionary, return a score of 0 for that letter
            score += 0

    # Return the final score
    return score

# Dictionary of letter values
letter_values = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10
}
