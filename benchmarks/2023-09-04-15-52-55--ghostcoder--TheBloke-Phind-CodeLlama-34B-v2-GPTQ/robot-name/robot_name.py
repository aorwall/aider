import random
import string

class Robot:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            self._generate_new_name()
        return self._name

    def _generate_new_name(self):
        letters = string.ascii_uppercase
        numbers = string.digits
        self._name = ''.join([random.choice(letters) for _ in range(2)] + [random.choice(numbers) for _ in range(3)])

    def reset_factory_settings(self):
        self._name = None
