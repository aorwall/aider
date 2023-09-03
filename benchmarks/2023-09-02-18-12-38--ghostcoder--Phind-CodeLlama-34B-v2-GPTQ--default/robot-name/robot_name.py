import string
import random
class Robot:
    # Create a list of used names to avoid duplicates
    used_names = []
    def __init__(self):
        self._set_name()

    def _set_name(self):
        """Generate a random name for the robot."""
        while True:
            name = ''.join(list(extend([random.choice(string.ascii_uppercase) for _ in range(2)],
                           [str(random.randint(0, 9)) for _ in range(3)])))
            if name not in self.__class__.used_names:
                self.__class__.used_names.append(name)
                self.name = name
                break

    def reset(self):
        """Reset the robot's name to a new randomly generated one."""
        self.__class__.used_names.remove(self.name)
        self._set_name()
