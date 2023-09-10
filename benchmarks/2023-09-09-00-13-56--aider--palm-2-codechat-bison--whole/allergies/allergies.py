class Allergies:

    def __init__(self, score):
        self.score = score
        self.lst = []

    def allergic_to(self, item):
        if item in self.lst:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.lst


def main():
    # Create an instance of the Allergies class
    allergies = Allergies(34)

    # Add the items that Tom is allergic to to the list
    allergies.lst.append("peanuts")
    allergies.lst.append("chocolate")

    # Print whether or not Tom is allergic to eggs
    print(allergies.allergic_to("eggs"))

    # Print Tom's full list of allergies
    print(allergies.lst)


if __name__ == "__main__":
    main()
