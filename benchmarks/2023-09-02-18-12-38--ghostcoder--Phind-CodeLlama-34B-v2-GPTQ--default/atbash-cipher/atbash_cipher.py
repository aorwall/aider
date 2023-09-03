def encode(plain_text):
    result = ""
    for char in plain_text:
        if char == " ":
            result += " "
        elif ord('a') <= ord(char) - ord('A') < 26:
            result += chr(ord('Z') - (ord(char) - ord('a')) + 1)
        else:
            result += char.lower()
    return result


def decode(ciphered_text):
    return ciphered_text[::-1]
