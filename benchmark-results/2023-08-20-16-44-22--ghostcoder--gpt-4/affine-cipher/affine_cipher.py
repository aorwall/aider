import math
import re

def encode(plain_text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text = re.sub('[^a-z0-9]', '', plain_text.lower())
    ciphered_text = [chr((a * (ord(c) - ord('a')) + b) % 26 + ord('a')) if c.isalpha() else c for c in plain_text]
    return ' '.join([''.join(ciphered_text[i:i+5]) for i in range(0, len(ciphered_text), 5)])

def decode(ciphered_text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    ciphered_text = re.sub('[^a-z0-9]', '', ciphered_text.lower())
    a_inv = pow(a, -1, 26)
    plain_text = [chr(a_inv * ((ord(c) - ord('a')) - b) % 26 + ord('a')) if c.isalpha() else c for c in ciphered_text]
    return ''.join(plain_text)