import random

class Robot:
    used_names = set()
    
    def __init__(self):
        self.name = self.generate_unique_name()

    def generate_name(self):
        letters = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
        numbers = random.sample('0123456789', 3)
        return ''.join(letters + numbers)

    def generate_unique_name(self):
        while True:
            name = self.generate_name()
            if name not in Robot.used_names:
                Robot.used_names.add(name)
                return name

    def reset(self):
        Robot.used_names.remove(self.name)
        self.name = self.generate_unique_name()
