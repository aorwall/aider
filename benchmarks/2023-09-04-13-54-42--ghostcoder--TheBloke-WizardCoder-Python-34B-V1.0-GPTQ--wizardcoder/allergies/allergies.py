class Allergies:

    ALLERGENS = {
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
        allergen_value = self.ALLERGENS.get(item)
        if allergen_value is None:
            raise ValueError('Invalid allergen')
        return bool(self.score & allergen_value)

    @property
    def lst(self):
        return [allergen for key, allergen in self.ALLERGENS.items() if self.allergic_to(key)]
