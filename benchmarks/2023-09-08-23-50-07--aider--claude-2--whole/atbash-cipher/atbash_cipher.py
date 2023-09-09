import string

alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]

def encode(plain_text):
    cipher_text = ""
    for char in plain_text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            cipher_char = reversed_alphabet[index]
            cipher_text += cipher_char
        else:
            cipher_text += char
    return cipher_text


def decode(ciphered_text):
    plain_text = ""
    for char in ciphered_text.lower():
        if char in reversed_alphabet:
            index = reversed_alphabet.index(char)
            plain_char = alphabet[index]
            plain_text += plain_char
        else:
            plain_text += char
    return plain_text.replace(" ", "")
