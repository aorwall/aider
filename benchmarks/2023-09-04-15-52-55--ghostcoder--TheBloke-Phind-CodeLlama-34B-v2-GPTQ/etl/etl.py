LETTER_VALUES = {
    "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10,
}

def transform(legacy_data):
    new_data = {}

    for word, score in legacy_data.items():
        for letter in str(word): # Convert int to string before iteration
            new_letter = letter.lower()

            if new_letter not in new_data:
                new_data[new_letter] = LETTER_VALUES[new_letter] * len([char for char in word if char == letter])

            else:
                new_data[new_letter] += LETTER_VALUES[new_letter] * len([char for char in word if char == letter])

    return new_data
