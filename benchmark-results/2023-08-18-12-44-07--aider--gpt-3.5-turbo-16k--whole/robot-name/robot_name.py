import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_random_name()

    def reset(self):
        self.name = self.generate_random_name()

    def generate_random_name(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        new_name = ''.join(letters + digits)
        while new_name == self.name:
            letters = random.choices(string.ascii_uppercase, k=2)
            digits = random.choices(string.digits, k=3)
            new_name = ''.join(letters + digits)
        return new_name
