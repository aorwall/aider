import string
from sympy import gcd

def encrypt(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    cipher_text = ""
    for char in plain_text:
        if char == " ":
            cipher_text += " "
        else:
            idx = (ord(char) - ord('A') + b) % 26
            cipher_text += chr((idx * a) % 26 + ord('A'))

    return cipher_text

def decrypt(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    a_inv = pow(a, -1, 26) # compute a^-1 modulo 26

    plain_text = ""
    for char in ciphered_text:
        if char == " ":
            plain_text += " "
        else:
            idx = ((ord(char) - ord('A')) * a_inv) % 26
            plain_text += chr((idx - b) % 26 + ord('A'))

    return plain_text