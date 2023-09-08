class Allergies:
    allergens = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return self.score & self.allergens.get(item, 0)

    @property
    def lst(self):
        return [allergen for allergen in self.allergens.values() if self.allergic_to(self.allergens[allergen])]
