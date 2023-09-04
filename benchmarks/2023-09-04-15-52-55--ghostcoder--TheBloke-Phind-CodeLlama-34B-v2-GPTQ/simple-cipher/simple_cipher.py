import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key.lower()

    def encode(self, text):
        encoded_text = ""
        for i, char in enumerate(text):
            if char.isalpha():
                offset = ord('a')
                index = (ord(char.lower()) - offset + len(self.key)) % 26
                encoded_text += chr(index + ord(self.key[(i % len(self.key))] .lower()))
            else:
                encoded_text += char
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for i, char in enumerate(text):
            if char.isalpha():
                offset = ord('a')
                index = (ord(char.lower()) - ord(self.key[(i % len(self.key))] .lower()) + 26) % 26
                decoded_text += chr(index + ord(self.key[index].lower()))
            else:
                decoded_text += char
        return decoded_text
