# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = "Ones"
TWOS = "Twos"
THREES = "Threes"
FOURS = "Fours"
FIVES = "Fives"
SIXES = "Sixes"
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
LITTLE_STRAIGHT = "Little Straight"
BIG_STRAIGHT = "Big Straight"
CHOICE = "Choice"


def score(dice, category):
    if category == YACHT:
        return score_yacht(dice)
    elif category == ONES:
        return score_ones(dice)
    elif category == TWOS:
        return score_twos(dice)
    elif category == THREES:
        return score_threes(dice)
    elif category == FOURS:
        return score_fours(dice)
    elif category == FIVES:
        return score_fives(dice)
    elif category == SIXES:
        return score_sixes(dice)
    elif category == FULL_HOUSE:
        return score_full_house(dice)
    elif category == FOUR_OF_A_KIND:
        return score_four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return score_little_straight(dice)
    elif category == BIG_STRAIGHT:
        return score_big_straight(dice)
    elif category == CHOICE:
        return score_choice(dice)
    else:
        return 0


def score_yacht(dice):
    if len(set(dice)) == 1:
        return 50
    else:
        return 0


def score_ones(dice):
    return dice.count(1)


def score_twos(dice):
    return dice.count(2) * 2


def score_threes(dice):
    return dice.count(3) * 3


def score_fours(dice):
    return dice.count(4) * 4


def score_fives(dice):
    return dice.count(5) * 5


def score_sixes(dice):
    return dice.count(6) * 6


def score_full_house(dice):
    counts = set(dice)
    if len(counts) == 2 and (dice.count(list(counts)[0]) == 2 or dice.count(list(counts)[0]) == 3):
        return sum(dice)
    else:
        return 0


def score_four_of_a_kind(dice):
    for i in set(dice):
        if dice.count(i) >= 4:
            return i * 4
    return 0


def score_little_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    else:
        return 0


def score_big_straight(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0


def score_choice(dice):
    return sum(dice)
