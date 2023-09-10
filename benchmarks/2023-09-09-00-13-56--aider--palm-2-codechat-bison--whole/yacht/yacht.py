# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1 * dice.count(1)
TWOS = 2 * dice.count(2)
THREES = 3 * dice.count(3)
FOURS = 4 * dice.count(4)
FIVES = 5 * dice.count(5)
SIXES = 6 * dice.count(6)
FULL_HOUSE = 2 * dice.count(1) + 3 * dice.count(2)
FOUR_OF_A_KIND = 4 * dice.count(1)
LITTLE_STRAIGHT = 1 + 2 + 3 + 4 + 5
BIG_STRAIGHT = 2 + 3 + 4 + 5 + 6
CHOICE = sum(dice)


def score(dice, category):
    if category == "Yacht":
        if dice.count(1) == 5 or dice.count(2) == 5 or dice.count(3) == 5 or dice.count(4) == 5 or dice.count(5) == 5 or dice.count(6) == 5:
            return YACHT
        else:
            return 0
    elif category == "Ones":
        return ONES
    elif category == "Twos":
        return TWOS
    elif category == "Threes":
        return THREES
    elif category == "Fours":
        return FOURS
    elif category == "Fives":
        return FIVES
    elif category == "Sixes":
        return SIXES
    elif category == "Full House":
        return FULL_HOUSE
    elif category == "Four of a Kind":
        return FOUR_OF_A_KIND
    elif category == "Little Straight":
        return LITTLE_STRAIGHT
    elif category == "Big Straight":
        return BIG_STRAIGHT
    elif category == "Choice":
        return CHOICE
    else:
        return 0
