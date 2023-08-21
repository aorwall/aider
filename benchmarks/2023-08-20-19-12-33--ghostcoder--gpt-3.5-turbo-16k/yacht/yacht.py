# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    elif category == ONES:
        return dice.count(1) * 1
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for i in set(dice):
            if dice.count(i) >= 4:
                return i * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if set(dice) == {1, 2, 3, 4, 5}:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if set(dice) == {2, 3, 4, 5, 6}:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0