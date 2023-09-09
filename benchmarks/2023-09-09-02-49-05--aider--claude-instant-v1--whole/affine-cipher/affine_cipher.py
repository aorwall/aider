import math

def encode(plain_text, a, b, m=26):
    if not math.gcd(a, m) == 1:
        raise ValueError("a and m must be coprime.")

    ciphered_text = ""
    for char in plain_text:
        if char.isalpha():
            char_index = ord(char) - ord('a')
            encrypted_char_index = (a * char_index + b) % m
            encrypted_char = chr(encrypted_char_index + ord('a'))
            ciphered_text += encrypted_char
        else:
            ciphered_text += char

    return ciphered_text


def decode(ciphered_text, a, b, m=26):
    if not math.gcd(a, m) == 1:
        raise ValueError("a and m must be coprime.")

    a_inverse = pow(a, -1, m)
    plain_text = ""
    for char in ciphered_text:
        if char.isalpha():
            char_index = ord(char) - ord('a')
            decrypted_char_index = (a_inverse * (char_index - b)) % m
            decrypted_char = chr(decrypted_char_index + ord('a'))
            plain_text += decrypted_char
        else:
            plain_text += char

    return plain_text
