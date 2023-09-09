import math

def encode(plain_text, a, b):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            i = ord(char) - ord('a') 
            cipher_i = (a * i + b) % 26
            cipher_char = chr(cipher_i + ord('a'))
            cipher_text += cipher_char
        else:
            cipher_text += char
    
    return cipher_text


def decode(ciphered_text, a, b):
    plain_text = ""
    a_inv = modinv(a, 26)
    if a_inv is None:
        raise ValueError("a and m must be coprime.")

    for char in ciphered_text:
        if char.isalpha():
            i = ord(char) - ord('a')
            plain_i = (a_inv * (i - b)) % 26
            plain_char = chr(plain_i + ord('a'))
            plain_text += plain_char
        else:
            plain_text += char

    return plain_text


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
