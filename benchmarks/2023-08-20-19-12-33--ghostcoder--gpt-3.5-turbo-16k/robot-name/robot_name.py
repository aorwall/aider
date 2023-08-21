import random
import string

class Robot:
    used_names = set()

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        while True:
            letters = random.choices(string.ascii_uppercase, k=2)
            digits = random.choices(string.digits, k=3)
            name = ''.join(letters + digits)
            if name not in self.used_names:
                self.used_names.add(name)
                return name

    def reset(self):
        self.name = self.generate_name()