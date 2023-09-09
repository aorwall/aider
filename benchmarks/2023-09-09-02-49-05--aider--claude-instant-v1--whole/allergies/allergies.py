class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = {
            "eggs": 1,
            "peanuts": 2,  
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16, 
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

    def allergic_to(self, item):
        item_score = self.allergies.get(item)
        return item_score is not None and self.score & item_score > 0

    @property
    def lst(self):
        return [name for name, score in self.allergies.items() if self.score & score > 0]
