import collections

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
    counts = [sum(i == di for i in range(1, 7)) for di in dice]

    if category == 'ONES':   return counts[0]*1
    if category == 'TWOS':   return counts[1]*2
    if category == 'THREES': return counts[2]*3
    if category == 'FOURS':  return counts[3]*4
    if category == 'FIVES':  return counts[4]*5
    if category == 'SIXES':  return counts[5]*6

    if category == 'FULL_HOUSE':
        if 3 in counts and 2 in counts: return sum(dice)
    if category == 'FOUR_OF_A_KIND':
        if max(counts) >= 4: return sum(dice)

    if category == 'LITTLE_STRAIGHT':
        return 30 if set(counts[:-1]) == {1} else 0
    if category == 'BIG_STRAIGHT':
        return 30 if set(counts) == {1} and counts[-1]==1 else 0

    if category == 'CHOICE':
        return sum(dice)

    if category == 'YACHT':
        return 50 if len(set(dice))==1 else 0

    return 0 # unknown category
