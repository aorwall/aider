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
        self.score = score

    def allergic_to(self, item):
        """Checks if the person is allergic to a specific item."""
        allergen_value = self.ALLERGENS.get(item, 0)
        return bool(allergen_value & self.score)

    @property
    def lst(self):
        """Returns a list of all the allergies the person has."""
        return [allergen for allergen, value in self.ALLERGENS.items() if value & self.score == value]
