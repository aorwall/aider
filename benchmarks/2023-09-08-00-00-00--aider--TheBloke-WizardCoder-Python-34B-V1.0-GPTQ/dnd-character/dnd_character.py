import random

class Character:
    def __init__(self):
        self.abilities = {
            "strength": self.roll_ability(),
            "dexterity": self.roll_ability(),
            "constitution": self.roll_ability(),
            "intelligence": self.roll_ability(),
            "wisdom": self.roll_ability(),
            "charisma": self.roll_ability()
        }
        self.hitpoints = 10 + self.get_constitution_modifier()

    def roll_ability(self):
        dice_rolls = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)
        return sum(dice_rolls[:3])

    def get_constitution_modifier(self):
        return -((self.abilities["constitution"] - 10) // 2)