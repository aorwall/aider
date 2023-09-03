import re
import uuid
class Robot:
    assigned_names = set()
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            while True:
                # Generate a new name until a unique one is found
                new_name = 'R' + str(uuid.uuid4())[:3].upper()  # R followed by three digits generated using uuid
                if new_name not in self.assigned_names:
                    self.assigned_names.add(new_name)
                    break
            self._name = new_name
        return self._name

    def reset(self):
        self._name = None

    @staticmethod
    def is_valid_name(name):
        """Checks whether a given name is valid or not"""
        name_re = re.compile('^[A-Z]{2}\\d{3}$')
        return bool(name_re.match(name))
