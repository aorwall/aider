import math

def is_coprime(a, m):
    return math.gcd(a, m) == 1

def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encode(plain_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    ciphered_text = ""
    for char in plain_text:
        if char.isalpha():
            index = ord(char) - ord('a')
            encrypted_index = (a * index + b) % 26
            encrypted_char = chr(encrypted_index + ord('a'))
            ciphered_text += encrypted_char
        elif char.isdigit():
            ciphered_text += char

    return ciphered_text

def decode(ciphered_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")

    decrypted_text = ""
    for char in ciphered_text:
        if char.isalpha():
            index = ord(char) - ord('a')
            decrypted_index = (modular_inverse(a, 26) * (index - b)) % 26
            decrypted_char = chr(decrypted_index + ord('a'))
            decrypted_text += decrypted_char
        elif char.isdigit():
            decrypted_text += char

    return decrypted_text
