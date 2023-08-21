import random

class Character:
    def __init__(self):
        self.strength = self.roll_ability()
        self.dexterity = self.roll_ability()
        self.constitution = self.roll_ability()
        self.intelligence = self.roll_ability()
        self.wisdom = self.roll_ability()
        self.charisma = self.roll_ability()
        self.hitpoints = 10 + self.get_modifier(self.constitution)

    def roll_ability(self):
        dice_rolls = [random.randint(1, 6) for _ in range(4)]
        dice_rolls.sort()
        return sum(dice_rolls[1:])

    def get_modifier(self, ability_score):
        return (ability_score - 10) // 2