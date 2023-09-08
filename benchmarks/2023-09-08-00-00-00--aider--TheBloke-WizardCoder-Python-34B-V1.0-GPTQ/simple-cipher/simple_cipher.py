import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=100))
        else:
            self.key = key.lower()

    def encode(self, text):
        encoded = ''
        for char in text:
            if char.isalpha():
                if char.isupper():
                    encoded += chr((ord(char) - 65 + self.key.index(self.key[0])) % 26 + 65)
                else:
                    encoded += chr((ord(char) - 97 + self.key.index(self.key[0])) % 26 + 97)
            else:
                encoded += char
        return encoded

    def decode(self, text):
        decoded = ''
        for char in text:
            if char.isalpha():
                if char.isupper():
                    decoded += chr((ord(char) - 65 - self.key.index(self.key[0])) % 26 + 65)
                else:
                    decoded += chr((ord(char) - 97 - self.key.index(self.key[0])) % 26 + 97)
            else:
                decoded += char
        return decoded
