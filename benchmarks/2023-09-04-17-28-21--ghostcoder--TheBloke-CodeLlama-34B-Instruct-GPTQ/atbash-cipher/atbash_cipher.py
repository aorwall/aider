import string

def encode(plain_text):
    # Create a dictionary to map each character to its corresponding encrypted character
    char_map = {chr(i+97): chr((26 - (i % 26)) + 97) for i in range(26)}

    # Replace each character in the plain text with its encrypted counterpart
    cipher_text = ''.join([char_map[c] for c in plain_text])

    # Group the characters into blocks of five and separate them by spaces
    cipher_text = ' '.join([cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)])

    return cipher_text

def decode(ciphered_text):
    # Create a dictionary to map each encrypted character to its corresponding decrypted character
    char_map = {chr((26 - (i % 26)) + 97): chr(i+97) for i in range(26)}

    # Replace each encrypted character in the cipher text with its decrypted counterpart
    plain_text = ''.join([char_map[c] for c in ciphered_text])

    return plain_text
