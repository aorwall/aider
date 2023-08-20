def encode(plain_text):
    plain_text = plain_text.lower()
    ciphered_text = ''
    for char in plain_text:
        if char.isalpha():
            ciphered_text += chr(219 - ord(char))
        elif char.isalnum():
            ciphered_text += char
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text):
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            plain_text += chr(219 - ord(char))
        elif char.isalnum():
            plain_text += char
    return plain_text.replace(' ', '')