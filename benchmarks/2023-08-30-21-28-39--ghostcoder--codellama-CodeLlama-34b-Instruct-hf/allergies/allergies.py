class Allergies:
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if self.score & item.value:
            return True
        return False

    @property
    def lst(self):
        lst = []
        for item in Allergen.items:
            if self.allergic_to(item):
                lst.append(item.name)
        return lst
