def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((ord(char) - base + key) % 26) + base)
        else:
            result += char
    return result
