import random

class Robot:
    def __init__(self):
        self.name = None

    def reset(self):
        self.name = None

    def get_name(self):
        if self.name is None:
            self.name = "".join(random.choice(string.ascii_uppercase) for _ in range(2)) + "".join(str(random.randint(0, 9)) for _ in range(3))
        return self.name
