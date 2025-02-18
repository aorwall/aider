import random
from math import floor

class Character:
    ABILITIES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self):
        self._abilities = {ability: self._generate_ability() for ability in self.ABILITIES}
        self.hitpoints = 10 + self._get_constitution_modifier()

    def _generate_ability(self):
        dice_throws = sorted([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])[-3:]
        return sum(dice_throws)

    def _get_constitution_modifier(self):
        con_score = self._abilities["constitution"]
        return floor((con_score - 10) / 2)

    @property
    def abilities(self):
        return self._abilities

    @property
    def constitution_modifier(self):
        return self._get_constitution_modifier()

    @property
    def modifier(self):
        return self._get_constitution_modifier()
