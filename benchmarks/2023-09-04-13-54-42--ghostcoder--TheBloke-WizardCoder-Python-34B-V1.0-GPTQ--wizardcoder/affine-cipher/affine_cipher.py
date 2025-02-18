import math
from typing import List

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    g = gcd(a, m)
    if g != 1:
        raise ValueError("a and m must be coprime.")
    else:
        return pow(a, -1, m)

def encode(plain_text: str, a: int, b: int) -> str:
    ciphered_text = ""

    for char in plain_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97

            encoded_char = chr(((a * (ord(char) - offset) + b) % 26) + offset)
            ciphered_text += encoded_char
        elif char == ' ':
            ciphered_text += ' '

    return ciphered_text


def decode(ciphered_text: str, a: int, b: int) -> str:
    a_inv = modinv(a, 26)
    plain_text = ""

    for char in ciphered_text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97

            decoded_char = chr(((a_inv * ((ord(char) - offset - b)) % 26)) + offset)
            plain_text += decoded_char
        elif char == ' ':
            plain_text += ' '

    return plain_text