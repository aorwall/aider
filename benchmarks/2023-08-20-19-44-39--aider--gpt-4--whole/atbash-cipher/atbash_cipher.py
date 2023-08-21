def encode(plain_text):
    ciphered_text = ''
    for char in plain_text.lower():
        if char.isalpha():
            ciphered_text += chr(219 - ord(char))
        elif char.isdigit():
            ciphered_text += char
    return ' '.join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))

def decode(ciphered_text):
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():
            plain_text += chr(219 - ord(char))
        elif char.isdigit():
            plain_text += char
    return plain_text.replace(' ', '')
