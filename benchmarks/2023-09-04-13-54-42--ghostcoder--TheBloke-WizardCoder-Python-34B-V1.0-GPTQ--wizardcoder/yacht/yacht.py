from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    # Check for invalid input
    if len(dice) != 5 or not all(isinstance(x, int) and x >= 1 and x <= 6 for x in dice):
        raise ValueError("Invalid input")

    # Calculate score based on category
    if category == ONES:
        return sum(v for v in dice if v == 1)
    elif category == TWOS:
        return sum(v for v in dice if v == 2) * 2
    elif category == THREES:
        return sum(v for v in dice if v == 3) * 3
    elif category == FOURS:
        return sum(v for v in dice if v == 4) * 4
    elif category == FIVES:
        return sum(v for v in dice if v == 5) * 5
    elif category == SIXES:
        return sum(v for v in dice if v == 6) * 6
    elif category == FULL_HOUSE:
        counts = Counter(dice)
        if len(counts) == 2 and (max(counts.values()) == 2 or max(counts.values()) == 3):
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        if len(counts) == 1 or (len(counts) == 2 and min(counts.values()) == 1):
            return counts.most_common()[0][0] * 4
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        sorted_dice = sorted(set(dice))
        return 30 if sorted_dice == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        sorted_dice = sorted(set(dice))
        return 30 if sorted_dice == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        counts = Counter(dice)
        return 50 if len(counts) == 1 else 0
    else:
        raise ValueError("Invalid category")
