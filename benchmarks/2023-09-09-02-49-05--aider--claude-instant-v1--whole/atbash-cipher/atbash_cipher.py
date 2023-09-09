def encode(plain_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    ciphered_text = ""
    for char in plain_text.lower():
        if char in alphabet or char.isdigit():
            if char.isdigit():
                ciphered_text += char
            else: 
                ciphered_text += cipher[alphabet.index(char)]
        else:
            ciphered_text += char
    return " ".join(ciphered_text[i:i+5] for i in range(0, len(ciphered_text), 5))


def decode(ciphered_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba" 
    plain_text = ""
    ciphered_text = ciphered_text.replace(" ", "")
    for char in ciphered_text:
        if char in cipher:
            plain_text += alphabet[cipher.index(char)]
        elif char.isdigit():
            plain_text += char
        else:
            plain_text += char
    return plain_text
