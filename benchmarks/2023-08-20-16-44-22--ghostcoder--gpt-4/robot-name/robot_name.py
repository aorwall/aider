import random
import string

class Robot:
    _names = set()

    def __init__(self):
        self.name = ''
        self.reset()

    def reset(self):
        while True:
            name = self._generate_random_name()
            if name not in self._names:
                break
        self._names.discard(self.name)
        self.name = name
        self._names.add(self.name)

    @staticmethod
    def _generate_random_name():
        letters = random.choices(string.ascii_uppercase, k=2)
        digits = random.choices(string.digits, k=3)
        return ''.join(letters + digits)