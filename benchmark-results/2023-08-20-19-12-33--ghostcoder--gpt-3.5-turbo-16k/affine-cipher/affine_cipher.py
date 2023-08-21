def encode(plain_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_text = ""
    for char in plain_text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            encoded_index = (a * index + b) % 26
            encoded_char = alphabet[encoded_index]
            encoded_text += encoded_char
        else:
            encoded_text += char
    return " ".join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_text = ""
    for char in ciphered_text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            decoded_index = (modular_multiplicative_inverse(a, 26) * (index - b)) % 26
            decoded_char = alphabet[decoded_index]
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text


def modular_multiplicative_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("a and m must be coprime.")