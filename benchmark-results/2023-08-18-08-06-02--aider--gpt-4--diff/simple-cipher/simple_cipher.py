import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded_text = ''
        for i in range(len(text)):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            encoded_char = chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
            encoded_text += encoded_char
        return encoded_text

    def decode(self, text):
        decoded_text = ''
        for i in range(len(text)):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded_char = chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
            decoded_text += decoded_char
        return decoded_text
