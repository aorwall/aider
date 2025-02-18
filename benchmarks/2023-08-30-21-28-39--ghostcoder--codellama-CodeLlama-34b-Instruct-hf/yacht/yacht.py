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
    # Initialize the score to 0
    score = 0

    # Check the category and calculate the score accordingly
    if category == YACHT:
        # Check if all dice have the same value
        if len(set(dice)) == 1:
            score = 50
    elif category == ONES:
        # Count the number of ones in the dice
        score = dice.count(1)
    elif category == TWOS:
        # Count the number of twos in the dice
        score = dice.count(2)
    elif category == THREES:
        # Count the number of threes in the dice
        score = dice.count(3)
    elif category == FOURS:
        # Count the number of fours in the dice
        score = dice.count(4)
    elif category == FIVES:
        # Count the number of fives in the dice
        score = dice.count(5)
    elif category == SIXES:
        # Count the number of sixes in the dice
        score = dice.count(6)
    elif category == FULL_HOUSE:
        # Check if there are three of a kind and two of a kind
        if len(set(dice)) == 2:
            score = sum(dice)
    elif category == FOUR_OF_A_KIND:
        # Check if there are four of a kind
        if len(set(dice)) == 1:
            score = sum(dice)
    elif category == LITTLE_STRAIGHT:
        # Check if the dice are in order (1-2-3-4-5)
        if sorted(dice) == [1, 2, 3, 4, 5]:
            score = 30
    elif category == BIG_STRAIGHT:
        # Check if the dice are in order (2-3-4-5-6)
        if sorted(dice) == [2, 3, 4, 5, 6]:
            score = 30
    elif category == CHOICE:
        # Sum the dice
        score = sum(dice)

    return score
