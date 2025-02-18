import random

class Character:
    def __init__(self):
        self._abilities = {}
        self.generate_abilities()
        self.calculate_hitpoints()

    def generate_abilities(self):
        for ability in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            roll = sorted([random.randint(1, 6) for _ in range(4)])[-3:]
            score = sum(roll)
            self._abilities[ability] = score

    def calculate_hitpoints(self):
        const = self._abilities["constitution"]
        self.hitpoints = max(10 + ((const - 10) // 2), 1)

    @property
    def strength(self):
        return self._abilities['strength']

    @property
    def dexterity(self):
        return self._abilities['dexterity']

    @property
    def constitution(self):
        return self._abilities['constitution']

    @property
    def intelligence(self):
        return self._abilities['intelligence']

    @property
    def wisdom(self):
        return self._abilities['wisdom']

    @property
    def charisma(self):
        return self._abilities['charisma']
