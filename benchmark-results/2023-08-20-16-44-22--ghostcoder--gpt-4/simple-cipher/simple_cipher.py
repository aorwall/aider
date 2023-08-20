import random
import string
import itertools

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        return ''.join(chr((ord(char) - ord('a') + ord(key_char) - ord('a')) % 26 + ord('a')) 
                       for char, key_char in zip(text, itertools.cycle(self.key)))

    def decode(self, text):
        return ''.join(chr((ord(char) - ord('a') - (ord(key_char) - ord('a')) + 26) % 26 + ord('a')) 
                       for char, key_char in zip(text, itertools.cycle(self.key)))