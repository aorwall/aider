import string
from math import gcd

def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    ciphered_text = []
    for char in plain_text:
        if char.isalpha():
            i = string.ascii_lowercase.index(char)
            ciphered_text.append(string.ascii_lowercase[(a * i + b) % 26])
        elif char.isdigit():
            ciphered_text.append(char)
    ciphered_text = ''.join(ciphered_text)
    ciphered_text = ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))
    return ciphered_text


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            y = string.ascii_lowercase.index(char)
            for i in range(26):
                if (a * i) % 26 == 1:
                    a_inv = i
                    break
            plain_text += string.ascii_lowercase[(a_inv * (y - b)) % 26]
        elif char.isdigit():
            plain_text += char
    return plain_text
