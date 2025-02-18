import string
import random
from typing import Set

class Robot:
    used_names: Set[str] = set()

    def __init__(self):
        if len(Robot.used_names) < 900: # There are only 900 possible combinations of letters and numbers
            self.name = ''.join([random.choice(string.ascii_uppercase), random.choice(string.digits)] + [str(random.randint(0, 9)) for _ in range(3)])
            while self.name in Robot.used_names:
                self.name = ''.join([random.choice(string.ascii_uppercase), random.choice(string.digits)] + [str(random.randint(0, 9)) for _ in range(3)])
            Robot.used_names.add(self.name)
        else:
            raise ValueError('No more available names')

    def reset(self):
        Robot.used_names.remove(self.name)
        self.__init__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in Robot.used_names:
            raise ValueError('Name already exists')
        elif len(value) != 5 or not (value[0].isalpha() and value[1].isalpha() and value[2:].isdigit()):
            raise ValueError('Invalid name format')
        else:
            self._name = value
            Robot.used_names.add(value)
