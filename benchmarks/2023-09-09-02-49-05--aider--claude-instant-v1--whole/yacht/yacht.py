# Score categories.
YACHT = 50  
ONES = 1
TWOS = 2
THREES = 3 
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 25  
FOUR_OF_A_KIND = 20
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = 0

def score(dice, category):
    dice_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for die in dice:
        dice_count[die] += 1

    if category == YACHT and len(set(dice)) == 1:
        return YACHT
    elif category == ONES:
        return dice_count[1]
    elif category == TWOS:
        return 2 * dice_count[2] 
    elif category == THREES:
        return 3 * dice_count[3]
    elif category == FOURS: 
        return 4 * dice_count[4]
    elif category == FIVES:
        return 5 * dice_count[5]
    elif category == SIXES:
        return 6 * dice_count[6]
    elif category == FULL_HOUSE:
        if 3 in dice_count.values() and 2 in dice_count.values():
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        for v in dice_count.values():
            if v >= 4:
                return 4 * int(v/4) * dice_count.keys()[dice_count.values().index(v)]
        return 0
    elif category in [LITTLE_STRAIGHT, BIG_STRAIGHT]:
        return 30 if sorted(dice) == list(range(min(dice), max(dice)+1)) else 0
    else:
        return sum(dice)
