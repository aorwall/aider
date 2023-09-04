from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = "Y"
ONES = "1"
TWOS = "2"
THREES = "3"
FOURS = "4"
FIVES = "5"
SIXES = "6"
FULL_HOUSE = "F"
FOUR_OF_A_KIND = "K"
LITTLE_STRAIGHT = "L"
BIG_STRAIGHT = "B"
CHOICE = "C"

def score(dice, category):
    counts = Counter(dice)

    if category == ONES:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == TWOS:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == THREES:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == FOURS:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == FIVES:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == SIXES:
        return sum([counts[i]*i for i in range(1, 7)])
    elif category == FULL_HOUSE:
        return 25 if len(set(counts.values()))==2 else 0
    elif category == FOUR_OF_A_KIND:
        return sum(key*value*5//4 for key, value in counts.items() if list(counts.keys())[-1]>=4)
    elif category == LITTLE_STRAIGHT:
        return 30 if set(range(1, 6)) <= set(dice) else 0
    elif category == BIG_STRAIGHT:
        return 30 if set(range(2, 7)) <= set(dice) else 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        return 50 if len(set(counts.values()))==1 else 0
    else:
        raise ValueError("Invalid category")
