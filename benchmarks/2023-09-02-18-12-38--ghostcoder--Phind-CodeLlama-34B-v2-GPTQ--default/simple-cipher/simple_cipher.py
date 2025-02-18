import string
from random import randint
class Cipher:
    def __init__(self, key=None):
        self._key = key
        if not self._key:
            self._key = ''.join(chr(randint(97, 122)) for _ in range(100))

    def encode(self, text):
        return "".join([chr((ord(char) - 97 + ord(self._key[i % len(self._key)])) % 26 + 97) if char.isalpha() else char
                       for i, char in enumerate(text.lower())])

    def decode(self, text):
        return "".join([chr((ord(char) - 97 - (ord(self._key[i % len(self._key)]))) % 26 + 97) if char.isalpha() else char
                       for i, char in enumerate(text.lower())])