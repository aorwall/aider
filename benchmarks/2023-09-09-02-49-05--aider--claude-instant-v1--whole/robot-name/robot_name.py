import random

class Robot:
    def __init__(self):
        self.name = self.generate_name()
        
    def generate_name(self):
        letters = "BCDEFGHJKLMNPQRSTVWXYZ"
        digits = "0123456789"
        name = ""
        for i in range(2):
            name += random.choice(letters)
        for i in range(3):
            name += random.choice(digits)
        return name

    def reset(self):
        self.name = self.generate_name()
