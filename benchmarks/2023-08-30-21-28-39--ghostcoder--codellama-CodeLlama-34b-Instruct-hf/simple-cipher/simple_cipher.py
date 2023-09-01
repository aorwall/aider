import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(100))
        self.key = key

    def encode(self, text):
        encoded_text = ''
        for i, c in enumerate(text):
            encoded_text += chr((ord(c) + self.key[i % len(self.key)]) % 26)
        return encoded_text

    def decode(self, text):
        decoded_text = ''
        for i, c in enumerate(text):
            decoded_text += chr((ord(c) - self.key[i % len(self.key)]) % 26)
        return decoded_text