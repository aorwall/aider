class Robot:
    def __init__(self):
        self.name = None
        self.name_dict = {}

    def generate_name(self):
        while True:
            name = ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(3))
            if name not in self.name_dict:
                self.name_dict[name] = True
                break
        self.name = name

    def reset(self):
        self.name = None
        self.name_dict = {}
