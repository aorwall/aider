import string
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def mod_inverse(a, m):
    for i in range(1, m):
        if (i * a) % m == 1:
            return i
    return None
def encode(plain_text, a, b):
    result = ""
    for char in plain_text:
        if char.isdigit():
            result += char
        elif char.isspace() or char in string.punctuation:
            continue
        else:
            index = ord(char.lower()) - 97
            encrypted_index = (a * index + b) % 26
            result += chr((encrypted_index + 65) if char.isupper() else (encrypted_index + 97))

    return " ".join([result[i:i+5] for i in range(0, len(result), 5)])


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    a_mmi = mod_inverse(a, 26)
    result = ""
    for char in ciphered_text:
        if char.isdigit():
            result += char
        elif char.isspace() or char in string.punctuation:
            continue
        else:
            index = ord(char.lower()) - 97
            decrypted_index = (a_mmi * (index - b)) % 26
            result += chr((decrypted_index + 65) if char.isupper() else (decrypted_index + 97))

    return result
