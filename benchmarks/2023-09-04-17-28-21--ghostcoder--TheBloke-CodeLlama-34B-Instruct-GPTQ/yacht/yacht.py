import collections

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
    counts = collections.Counter(dice)
    max_count = max(counts.values())
    min_count = min(counts.values())

    # Yacht
    if category == YACHT and len(set(dice)) == 1:
        return YACHT

    # Ones, Twos, Threes, Fours, Fives, Sixes
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        count = counts[category]
        return count * category

    # Full House
    elif category == FULL_HOUSE and max_count >= 3 and min_count >= 2:
        return sum(dice)

    # Four of a Kind
    elif category == FOUR_OF_A_KIND and max_count >= 4:
        return 4 * [max(counts)] + list({k: v for k, v in counts.items() if v < 4}.values())

    # Little Straight
    elif category == LITTLE_STRAIGHT and set(range(1, 6)).issubset(counts.keys()):
        return LITTLE_STRAIGHT

    # Big Straight
    elif category == BIG_STRAIGHT and set(range(2, 7)).issubset(counts.keys()):
        return BIG_STRAIGHT

    # Choice
    elif category == CHOICE:
        return sum(dice)

    else:
        return 0
