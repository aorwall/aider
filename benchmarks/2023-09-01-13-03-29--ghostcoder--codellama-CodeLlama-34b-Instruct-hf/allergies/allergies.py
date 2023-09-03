class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        value = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }
        return self.score & value[item]

    @property
    def lst(self):
        return [k for k, v in value.items() if self.score & v]