import string
from random import randint

class Cipher:

    def __init__(self, key=None):
        self.alphabet = list(string.ascii_lowercase)
        if key is None:
            self.key = randint(1, len(self.alphabet))
        else:
            self.key = key

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char not in self.alphabet:
                continue # skip non-alphabetic characters
            index = (self.alphabet.index(char) + self.key) % len(self.alphabet)
            encoded_text += self.alphabet[index]
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for char in text:
            if char not in self.alphabet:
                continue # skip non-alphabetic characters
            index = (self.alphabet.index(char) - self.key) % len(self.alphabet)
            decoded_text += self.alphabet[index]
        return decoded_text
