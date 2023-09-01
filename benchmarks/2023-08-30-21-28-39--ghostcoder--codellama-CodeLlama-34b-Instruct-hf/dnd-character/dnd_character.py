class Character:
    def __init__(self):
        self.abilities = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }
        self.hitpoints = 0

    def roll_dice(self, num_dice, num_sides):
        rolls = []
        for i in range(num_dice):
            rolls.append(random.randint(1, num_sides))
        rolls.sort()
        return sum(rolls[-3:])

    def generate_character(self):
        for ability in self.abilities:
            self.abilities[ability] = self.roll_dice(4, 6)
        self.hitpoints = 10 + self.abilities["constitution"] // 2

# Test the generate_character function
character = Character()
character.generate_character()
print(character.abilities)
print(character.hitpoints)