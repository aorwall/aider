import random
class Character:
    def __init__(self):
        self._abilities = {
            'strength': self._roll(),
            'dexterity': self._roll(),
            'constitution': self._roll(),
            'intelligence': self._roll(),
            'wisdom': self._roll(),
            'charisma': self._roll()
        }

        self.hitpoints = 10 + self._calc_modifier(self._abilities['constitution'])

    @staticmethod
    def _roll():
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[-3:])

    @staticmethod
    def _calc_modifier(score):
        return (score - 10) // 2
