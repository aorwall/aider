def encode(plain_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    encoded_text = ""
    for char in plain_text:
        if char.isalpha():
            char_index = ord(char.lower()) - ord('a')
            encoded_index = (a * char_index + b) % 26
            encoded_char = chr(encoded_index + ord('a'))
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text


def decode(ciphered_text, a, b):
    if not is_coprime(a, 26):
        raise ValueError("a and m must be coprime.")
    decoded_text = ""
    for char in ciphered_text:
        if char.isalpha():
            char_index = ord(char.lower()) - ord('a')
            decoded_index = (modular_multiplicative_inverse(a, 26) * (char_index - b)) % 26
            if decoded_index < 0:
                decoded_index += 26
            decoded_char = chr(decoded_index + ord('a'))
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text


def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


def modular_multiplicative_inverse(a, m):
    if not is_coprime(a, m):
        raise ValueError("a and m must be coprime.")
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
