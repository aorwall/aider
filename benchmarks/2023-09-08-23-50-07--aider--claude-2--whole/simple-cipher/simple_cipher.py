import random

class Cipher:

    def __init__(self, key=None):
        if key is None: 
            self.key = self.generate_key()
        else:
            self.key = key

    def encode(self, text):
        encoded = ""
        for char in text:
            if char.isalpha():
                offset = ord(char) + self.key
                if char.islower():
                    if offset > ord('z'):
                        offset -= 26
                    elif offset < ord('a'):
                        offset += 26 
                elif char.isupper():
                    if offset > ord('Z'):
                        offset -= 26
                    elif offset < ord('A'):
                        offset += 26
                encoded += chr(offset)
            else:
                encoded += char
        return encoded

    def decode(self, text):
        return self.encode(text)

    def generate_key(self):
        self.key = random.randint(1, 25)
        return self.key
