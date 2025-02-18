class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        # Check if the item is in the list of allergies
        if item in self.lst:
            return True
        else:
            return False

    @property
    def lst(self):
        # Create a dictionary of allergies and their values
        allergies = {
            1: "eggs",
            2: "peanuts",
            4: "shellfish",
            8: "strawberries",
            16: "tomatoes",
            32: "chocolate",
            64: "pollen",
            128: "cats"
        }

        # Initialize an empty list to store the allergies
        lst = []

        # Loop through each bit in the binary representation of the score
        for i in bin(self.score)[2:]:
            # If the current bit is set, add the corresponding allergy to the list
            if int(i) == 1:
                lst.append(allergies[int(i)])

        return lst
