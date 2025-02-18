def encode(plain_text, a, b):
    cipher_text = ""
    for char in plain_text:
        # Encoding uppercase characters
        if char.isupper():
            encoded_num = ((a * (ord(char) - ord('A')) + b)) % 26
            cipher_text += chr(encoded_num + ord('A'))
        # Encoding lowercase characters
        else:
            encoded_num = ((a * (ord(char) - ord('a')) + b)) % 26
            cipher_text += chr(encoded_num + ord('a'))
    return cipher_text


def decode(ciphered_text, a, b):
    plain_text = ""
    mod_inv = get_mod_inv(a, 26)
    for char in ciphered_text:
        # Decoding uppercase characters
        if char.isupper():
            decoded_num = ((mod_inv * (ord(char) - ord('A') - b))) % 26
            plain_text += chr(decoded_num + ord('A'))
        # Decoding lowercase characters
        else:
            decoded_num = ((mod_inv * (ord(char) - ord('a') - b))) % 26
            plain_text += chr(decoded_num + ord('a'))
    return plain_text


def get_mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
