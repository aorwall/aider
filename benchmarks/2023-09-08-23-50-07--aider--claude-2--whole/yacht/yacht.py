# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3  
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 0
FOUR_OF_A_KIND = 0
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = 0


def score(dice, category):

    counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    for value in dice:
        counts[value] += 1
    
    if category == ONES:
        return counts[1]
    elif category == TWOS:
        return 2 * counts[2]
    elif category == THREES:
        return 3 * counts[3]
    elif category == FOURS:
        return 4 * counts[4]
    elif category == FIVES:
        return 5 * counts[5]
    elif category == SIXES:
        return 6 * counts[6]
    elif category == FULL_HOUSE:
        if 2 in counts.values() and 3 in counts.values():
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for value, count in counts.items():
            if count >= 4:
                return value * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1,2,3,4,5]:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2,3,4,5,6]:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    else:
        return 0
