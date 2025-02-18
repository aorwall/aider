import string
from typing import List

def rotate(text: str, key: int) -> str:
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    # Create a dictionary to store the mappings of characters to their rotated counterparts
    rotation_dict = {}
    for char in lowercase_letters:
        index = (lowercase_letters.index(char) + key) % 26
        rotation_dict[char] = lowercase_letters[index]

        # Handle uppercase letters
        uppercase_version = char.upper()
        rotation_dict[uppercase_version] = lowercase_letters[index].upper()

    # Split the text into words and iterate through each character
    words = text.split(' ')
    rotated_words = []
    for word in words:
        rotated_word = ''
        for char in word:
            if char in rotation_dict:
                rotated_word += rotation_dict[char]
            else:
                rotated_word += char

        rotated_words.append(rotated_word)

    return ' '.join(rotated_words)

# Test cases
print(rotate('omg', 5))  # Output: trl
print(rotate('c', 0))   # Output: c
print(rotate('Cool', 26))  # Output: Cool
print(rotate('The quick brown fox jumps over the lazy dog.', 13))  # Output: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
print(rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.', 13))  # Output: The quick brown fox jumps over the lazy dog.