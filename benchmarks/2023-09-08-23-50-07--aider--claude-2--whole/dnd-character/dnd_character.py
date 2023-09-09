import random

class Character:
    def __init__(self):
        self.abilities = {}
        self.hitpoints = 0
        
        for ability in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            self.abilities[ability] = sum(rolls)
        
        con_modifier = self.modifier(self.abilities["constitution"])
        self.hitpoints = 10 + con_modifier

    def modifier(self, value):
        return (value - 10) // 2
