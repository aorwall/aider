import random

class Character:
    def __init__(self):
        self.strength = self.roll_dice()
        self.dexterity = self.roll_dice()
        self.constitution = self.roll_dice()
        self.intelligence = self.roll_dice()
        self.wisdom = self.roll_dice()
        self.charisma = self.roll_dice()

    def roll_dice(self):
        dice = [random.randint(1, 6) for _ in range(4)]
        dice.sort(reverse=True)
        return sum(dice[:3])

    def get_hitpoints(self):
        return 10 + self.constitution_modifier()

    def constitution_modifier(self):
        return int(self.constitution - 10) // 2
