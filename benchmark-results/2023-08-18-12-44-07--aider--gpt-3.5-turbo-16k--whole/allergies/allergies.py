class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
        return item in allergens and self.score & allergens[item] != 0

    @property
    def lst(self):
        allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }
        return [item for item in allergens if self.score & allergens[item] != 0]
