import string
import random
from typing import Optional
class Cipher:
    def __init__(self, key: str = None):
        if not key:
            self._key = self._generate_key()
        else:
            self._key = key

    @staticmethod
    def _generate_key(length=100) -> str:
        import secrets
        return ''.join([secrets.choice(string.ascii_lowercase) for _ in range(length)])

    def encode(self, text: str) -> str:
        encoded = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + ord(self._key[key_index % len(self._key)] - ord('a')) % 26 + ord('a'))
                encoded += shifted_char
                key_index += 1
            else:
                encoded += char
        return encoded

    def decode(self, text: str) -> str:
        decoded = ''
        key_index = 0
        for char in text:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord(self._key[key_index % len(self._key)) + ord('a')) % 26 + ord('a'))
                decoded += shifted_char
                key_index += 1
            else:
                decoded += char
        return decoded

    @property
    def key(self) -> str:
        return self._key
