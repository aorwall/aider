import uuid

class Robot:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if not self._name:
            self._name = f"R{uuid.uuid4()}"[:5].upper()
        return self._name

    def reset(self):
        self._name = None
