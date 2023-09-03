# Score categories.
# Change the values as you see fit.
YACHT = 'yacht'
ONES = 'ones'
TWOS = 'twos'
THREES = 'threes'
FOURS = 'fours'
FIVES = 'fives'
SIXES = 'sixes'
FULL_HOUSE = 'full house'
FOUR_OF_A_KIND = 'four of a kind'
LITTLE_STRAIGHT = 'little straight'
BIG_STRAIGHT = 'big straight'
CHOICE = 'choice'


def count_occurrences(dice):
    """Count occurrences of each number in the dice."""
    counts = {}
    for num in range(1, 7):
        counts[num] = 0
    for die in dice:
        counts[die] += 1
    return counts


def score(dice, category):
    # Sort the dice so we can check for straights easily.
    sorted_dice = sorted(dice)

    def all_same():
        return len(set(dice)) == 1

    def full_house():
        counts = count_occurrences(dice)
        return (all_same() or set(counts.values()) == {2, 3}) and sum(counts.values()) == 5

    def little_straight():
        return sorted_dice == [1, 2, 3, 4, 5]

    def big_straight():
        return sorted_dice == [2, 3, 4, 5, 6]

    def choice():
        return sum(dice)

    def yacht():
        return 50 if all_same() else 0

    def ones():
        return dice.count(1) * 1

    def twos():
        return dice.count(2) * 2

    def threes():
        return dice.count(3) * 3

    def fours():
        return dice.count(4) * 4

    def fives():
        return dice.count(5) * 5

    def sixes():
        return dice.count(6) * 6

    switcher = {
        YACHT: yacht,
        ONES: ones,
        TWOS: twos,
        THREES: threes,
        FOURS: fours,
        FIVES: fives,
        SIXES: sixes,
        FULL_HOUSE: lambda: 25 if full_house() else 0,
        LITTLE_STRAIGHT: lambda: 30 if little_straight() else 0,
        BIG_STRAIGHT: lambda: 30 if big_straight() else 0,
        CHOICE: choice,
    }

    return switcher.get(category, lambda: 0)()
