def encode(plain_text):
    ciphered_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    for char in plain_text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            ciphered_text += reverse_alphabet[index]
        else:
            ciphered_text += char
    return ciphered_text

def decode(ciphered_text):
    plain_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    for char in ciphered_text.lower():
        if char.isalpha():
            index = reverse_alphabet.index(char)
            plain_text += alphabet[index]
        else:
            plain_text += char
    return plain_text
