import random
import string

class Robot:
    def __init__(self):
        self.name = None

    def reset(self):
        self.name = self._generate_name()

    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_name()
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def _generate_name(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        return ''.join(letters + numbers)
