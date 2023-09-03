def encode(plain_text):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            cipher_text += chr(219 - ord(char))
        else:
            cipher_text += char
    return cipher_text

def decode(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            plain_text += chr(219 - ord(char))
        else:
            plain_text += char
    return plain_text


def decode(ciphered_text):
    pass
