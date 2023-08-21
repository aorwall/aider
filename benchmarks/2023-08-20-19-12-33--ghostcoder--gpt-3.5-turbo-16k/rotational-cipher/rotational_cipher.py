def rotate(text, key):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                cipher_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text