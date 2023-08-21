class Allergies:
    ALLERGENS = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score & 255

    def allergic_to(self, item):
        return bool(self.score & self.ALLERGENS[item])

    @property
    def lst(self):
        return [item for item, value in self.ALLERGENS.items() if self.score & value]