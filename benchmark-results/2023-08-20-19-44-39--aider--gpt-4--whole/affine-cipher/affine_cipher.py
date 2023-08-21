import string
from math import gcd

def encode(plain_text, a, b):
    m = 26
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    ciphered_text = ''
    for i, char in enumerate(plain_text):
        if char.isalpha():
            i = string.ascii_lowercase.index(char)
            ciphered_text += string.ascii_lowercase[(a * i + b) % m]
        elif char.isdigit():
            ciphered_text += char
        if (i + 1) % 5 == 0:
            ciphered_text += ' '
    return ciphered_text.rstrip()  # remove trailing space

def decode(ciphered_text, a, b):
    m = 26
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            y = string.ascii_lowercase.index(char)
            for x in range(m):
                if (a * x) % m == 1:
                    a_inv = x
                    break
            plain_text += string.ascii_lowercase[(a_inv * (y - b)) % m]
        elif char.isdigit():
            plain_text += char
    return plain_text
