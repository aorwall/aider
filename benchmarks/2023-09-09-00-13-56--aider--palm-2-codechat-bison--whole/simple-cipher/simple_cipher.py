import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(random.choice(string.lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        return "".join(self.key.index(c) for c in text)

    def decode(self, text):
        return "".join(self.key[i] for i in text)
