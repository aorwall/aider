import uuid

used_names = set()

class Robot:
    """Represents a robot with a unique name."""

    def __init__(self):
        self._name = None

    @property
    def name(self):
        """Returns the robot's name.
        
        If no name has been assigned yet, generates a new name using UUID and ensures it hasn't already been taken.
        """
        if not self._name:
            # Generate a new name if one doesn't exist yet
            while True:
                candidate = f"R{str(uuid.uuid4())[:3].upper()}"
                if candidate not in used_names:
                    self._name = candidate
                    used_names.add(candidate)
                    break

        return self._name

    def reset(self):
        """Resets the robot's name to None, allowing for generation of a new name on next access."""
        self._name = None
