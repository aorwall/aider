import string
import random

class Cipher:
    def __init__(self, key=None):
        self.alphabet = string.ascii_lowercase
        if key is None:
            self.key = ''.join(random.choice(self.alphabet) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        encoded_text = ''
        for i in range(len(text)):
            shift = self.alphabet.index(self.key[i % len(self.key)])
            encoded_text += self.alphabet[(self.alphabet.index(text[i]) + shift) % len(self.alphabet)]
        return encoded_text

    def decode(self, text):
        decoded_text = ''
        for i in range(len(text)):
            shift = self.alphabet.index(self.key[i % len(self.key)])
            decoded_text += self.alphabet[(self.alphabet.index(text[i]) - shift) % len(self.alphabet)]
        return decoded_text
