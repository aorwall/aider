def encode(plain_text):
    plain_text = plain_text.replace(' ', '')
    cipher_text = ""

    for i in range(0, len(plain_text), 5):
        chunk = plain_text[i : i + 5]
        cipher_chunk = ""

        for char in chunk:
            if 'a' <= char <= 'z':
                index = ord('a') - ord(char)
                cipher_char = chr(index % 26 + ord('A'))
                cipher_chunk += cipher_char
            else:
                cipher_chunk += char

        cipher_text += cipher_chunk + " "

    return cipher_text[:-1] # Remove trailing space


def decode(ciphered_text):
    decoded_text = ""

    for i in range(0, len(ciphered_text), 6):
        chunk = ciphered_text[i : i + 6].rstrip()
        decoded_chunk = ""

        for char in chunk:
            if 'A' <= char <= 'Z':
                index = ord(char) - ord('A')
                decoded_char = chr(index % 26 + ord('a'))
                decoded_chunk += decoded_char
            else:
                decoded_chunk += char

        decoded_text += decoded_chunk

    return decoded_text
