def rotate(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) + key - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result
