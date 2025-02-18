class Allergies:
    def __init__(self, score):
        self.score = score
        self.allergens = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats'}

    def allergic_to(self, item):
        mask = 2 ** (item - 1)
        return bool(self.score & mask)

    @property
    def lst(self):
        return [allergen for i in range(1, len(self.allergens)+1) if self.allergic_to(i)]
