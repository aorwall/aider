class ZebraPuzzle:
    def __init__(self):
        self.houses = [
            {"color": "red", "nationality": "Englishman", "pet": None, "drink": None, "cigarette": None},
            {"color": "green", "nationality": None, "pet": None, "drink": "coffee", "cigarette": None},
            {"color": "yellow", "nationality": None, "pet": None, "drink": None, "cigarette": "Kools"},
            {"color": "blue", "nationality": None, "pet": None, "drink": None, "cigarette": None},
            {"color": "ivory", "nationality": None, "pet": None, "drink": None, "cigarette": None},
        ]

    def solve(self):
        for house in self.houses:
            if house["nationality"] == "Ukrainian" and house["drink"] == "tea":
                house["drink"] = "water"

            if house["pet"] == "zebra":
                self.zebra_owner = house

    def get_water_drinker(self):
        for house in self.houses:
            if house["drink"] == "water":
                return house["nationality"]

    def get_zebra_owner(self):
        return self.zebra_owner["nationality"]

def drinks_water():
    puzzle = ZebraPuzzle()
    puzzle.solve()
    return puzzle.get_water_drinker()

def owns_zebra():
    puzzle = ZebraPuzzle()
    puzzle.solve()
    return puzzle.get_zebra_owner()
