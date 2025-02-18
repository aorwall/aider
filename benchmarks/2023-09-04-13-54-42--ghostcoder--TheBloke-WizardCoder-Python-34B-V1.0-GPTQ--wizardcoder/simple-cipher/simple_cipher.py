import random
from typing import Optional

class Cipher:
    def __init__(self, key: str = None):
        self._key = key or ''.join([chr(random.randint(ord('a'), ord('z'))) for _ in range(100)])

    @property
    def key(self) -> str:
        return self._key

    def encode(self, plaintext: str) -> str:
        encoded = ''
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shifted_value = (ord(char) - ord('a') + ord(self.key[key_index])) % 26
                new_char = chr(shifted_value + ord('a'))
                key_index = (key_index + 1) % len(self.key)
            else:
                new_char = char

            encoded += new_char

        return encoded

    def decode(self, ciphertext: str) -> str:
        decoded = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                unshifted_value = (ord(char) - ord(self.key[key_index])) % 26
                new_char = chr(unshifted_value + ord('a'))
                key_index = (key_index + 1) % len(self.key)
            else:
                new_char = char

            decoded += new_char

        return decoded
