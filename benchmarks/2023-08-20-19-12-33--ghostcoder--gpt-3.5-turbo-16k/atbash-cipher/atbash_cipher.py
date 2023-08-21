def encode(plain_text):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            # Calculate the position of the character in the alphabet
            position = ord(char) - ord('a')
            # Calculate the position of the character in the reversed alphabet
            reversed_position = 25 - position
            # Convert the reversed position back to a character
            reversed_char = chr(reversed_position + ord('a'))
            # Append the reversed character to the cipher text
            cipher_text += reversed_char
        elif char.isdigit():
            # Append the digit to the cipher text
            cipher_text += char
    # Group the cipher text into groups of 5 characters
    grouped_cipher_text = ' '.join([cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)])
    return grouped_cipher_text


def decode(ciphered_text):
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            # Calculate the position of the character in the reversed alphabet
            reversed_position = ord(char) - ord('a')
            # Calculate the position of the character in the alphabet
            position = 25 - reversed_position
            # Convert the position back to a character
            plain_char = chr(position + ord('a'))
            # Append the plain character to the plain text
            plain_text += plain_char
        elif char.isdigit():
            # Append the digit to the plain text
            plain_text += char
    return plain_text