def encode(plain_text):
    cipher_text = ""
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
        else:
            # Append non-alphabetic characters as is
            cipher_text += char
    return cipher_text.strip()


def decode(ciphered_text):
    plain_text = ""
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
        else:
            # Append non-alphabetic characters as is
            plain_text += char
    return plain_text.strip()
