LETTERSCORE = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
    'e': 1,
    'f': 4,
    'g': 2,
    'h': 4,
    'i': 1,
    'j': 8,
    'k': 5,
    'l': 1,
    'm': 3,
    'n': 1,
    'o': 1,
    'p': 3,
    'q': 10,
    'r': 1,
    's': 1,
    't': 1,
    'u': 1,
    'v': 4,
    'w': 4,
    'x': 8,
    'y': 4,
    'z': 10
}

def score(word):
    # Convert all letters to lowercase
    word = word.lower()

    # Initialize variables
    total_score = 0
    prev_letter = None
    num_consecutive = 1

    # Iterate over the letters in the word
    for letter in word:
        # Check if this letter has a multiplier applied
        if letter == prev_letter:
            num_consecutive += 1
        else:
            # Add previous letter's score based on its count
            if prev_letter is not None:
                total_score += LETTERSCORE[prev_letter] * num_consecutive
            num_consecutive = 1

        # Update the previous letter and its count
        prev_letter = letter

    # Add last letter's score
    total_score += LETTERSCORE[prev_letter] * num_consecutive

    return total_score
