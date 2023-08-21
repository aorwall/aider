import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(random.choices(string.ascii_lowercase, k=100))
        self.key = key

    def encode(self, text):
        encoded_text = ''
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_text += encoded_char
        return encoded_text

    def decode(self, text):
        decoded_text = ''
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded_text += decoded_char
        return decoded_text
