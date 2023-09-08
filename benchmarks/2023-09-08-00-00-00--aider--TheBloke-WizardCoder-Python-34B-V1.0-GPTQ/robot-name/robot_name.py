import random
import string

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        letters = string.ascii_uppercase
        digits = string.digits
        name = ''.join(random.choice(letters) for _ in range(2)) + ''.join(random.choice(digits) for _ in range(3))
        return name

    def reset(self):
        self.name = self.generate_name()
