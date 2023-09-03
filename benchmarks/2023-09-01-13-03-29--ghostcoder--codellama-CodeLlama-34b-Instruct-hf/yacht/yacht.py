# Score categories.
# Change the values as you see fit.
YACHT = None
ONES = None
TWOS = None
THREES = None
FOURS = None
FIVES = None
SIXES = None
FULL_HOUSE = None
FOUR_OF_A_KIND = None
LITTLE_STRAIGHT = None
BIG_STRAIGHT = None
CHOICE = None


def score(dice, category):
    # Check if the dice are sorted
    if not is_sorted(dice):
        dice.sort()

    # Check if the dice have duplicates
    if has_duplicates(dice):
        return 0

    # Check if the dice are consecutive
    if not is_consecutive(dice):
        return 0

    # Calculate the score
    score = 0
    for i in range(len(dice)):
        score += dice[i]

    return score

def is_sorted(dice):
    for i in range(len(dice) - 1):
        if dice[i] > dice[i + 1]:
            return False
    return True

def has_duplicates(dice):
    return len(dice) != len(set(dice))

def is_consecutive(dice):
    for i in range(len(dice) - 1):
        if dice[i] + 1 != dice[i + 1]:
            return False
    return True
