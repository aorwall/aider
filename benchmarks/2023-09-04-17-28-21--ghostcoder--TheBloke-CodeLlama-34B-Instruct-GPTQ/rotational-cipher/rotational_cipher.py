import string

def rotate(text, key):
    """
    Takes a string and a rotation key. Returns the encrypted text.
    """
    # Create a dictionary to map each character to its corresponding encrypted character
    char_map = {}
    for i in range(len(string.ascii_letters)):
        char_map[string.ascii_letters[i]] = string.ascii_letters[(i+key) % len(string.ascii_letters)]

    # Encrypt the text by replacing each character with its corresponding encrypted character
    encrypted_text = ""
    for char in text:
        encrypted_text += char_map[char]

    return encrypted_text
