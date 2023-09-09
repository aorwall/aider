import random

class Character:

    def __init__(self):
        self.strength = self.roll_ability() 
        self.dexterity = self.roll_ability()
        self.constitution = self.roll_ability() 
        self.intelligence = self.roll_ability()
        self.wisdom = self.roll_ability()
        self.charisma = self.roll_ability()

        self.hitpoints = 10 + self.calculate_hitpoints()

    def roll_ability(self):
        rolls = [random.randint(1,6) for i in range(4)]
        rolls.sort(reverse=True)
        return sum(rolls[:3])

    def calculate_hitpoints(self):
        constitution = self.constitution
        modifier = self.get_modifier(constitution)
        return int(10 + modifier)

    def get_modifier(self, ability_score):
        if ability_score >= 10:
            return 0
        return int((ability_score - 10) / 2)
