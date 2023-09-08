# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = 11

def score(dice, category):
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return dice.count(1) * ONES
    elif category == TWOS:
        return dice.count(2) * TWOS
    elif category == THREES:
        return dice.count(3) * THREES
    elif category == FOURS:
        return dice.count(4) * FOURS
    elif category == FIVES:
        return dice.count(5) * FIVES
    elif category == SIXES:
        return dice.count(6) * SIXES
    elif category == FULL_HOUSE:
        counts = Counter(dice)
        return sum(dice) if set(counts.values()) == {2, 3} else 0
    elif category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        return counts.most_common(1)[0][0] * 4 if counts.most_common(1)[0][1] == 4 else 0
    elif category == LITTLE_STRAIGHT:
        return LITTLE_STRAIGHT if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return BIG_STRAIGHT if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)

class Yacht:
    def score(self, dice, category):
        return score(dice, category)
