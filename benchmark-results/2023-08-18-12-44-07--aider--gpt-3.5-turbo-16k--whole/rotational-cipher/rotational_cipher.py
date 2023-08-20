def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            shifted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result
