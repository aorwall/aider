import string

def encode(plain_text):
    plain_text = plain_text.lower()
    ciphered_text = ''
    for char in plain_text:
        if char.isalpha():
            ciphered_text += chr(219 - ord(char))
        elif char.isnumeric():
            ciphered_text += char
    ciphered_text = ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))
    return ciphered_text

def decode(ciphered_text):
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            plain_text += chr(219 - ord(char))
        elif char.isnumeric():
            plain_text += char
    return plain_text
