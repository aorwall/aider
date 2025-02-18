import random

class Character:
    def __init__(self):
        # Roll six 4-sided dice and keep the highest three values
        self.strength = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])
        self.dexterity = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])
        self.constitution = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])
        self.intelligence = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])
        self.wisdom = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])
        self.charisma = max([sum(sorted(random.sample(range(1, 7), 4))[-3:]) for _ in range(6)])

        # Calculate hit points based on constitution score
        self.hit_points = 10 + ((self.constitution - 10) // 2)

    @property
    def ability_scores(self):
        """Return a dictionary containing all ability scores."""
        return {
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Constitution": self.constitution,
            "Intelligence": self.intelligence,
            "Wisdom": self.wisdom,
            "Charisma": self.charisma,
        }

    @property
    def non_zero_ability_scores(self):
        """Return a dictionary containing only non-zero ability scores."""
        return {k: v for k, v in self.ability_scores.items() if v != 0}

    def __repr__(self):
        """Return a string representation of the character."""
        return f"Character({', '.join(f'{key}={value}' for key, value in self.non_zero_ability_scores.items())})"

if __name__ == '__main__':
    print(Character())
