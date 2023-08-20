import itertools

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((nationalities[WATER-1], nationalities[ZEBRA-1])
                for (red, green, ivory, yellow, blue) in orderings
                if imright(houses.index(ivory), houses.index(green)) # 6
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                if Englishman == red # 2
                if Norwegian == first # 10
                if nextto(houses.index(Norwegian), houses.index(blue)) # 15
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee == green # 4
                if Ukrainian == tea # 5
                if milk == middle # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools == yellow # 8
                if LuckyStrike == oj # 13
                if Japanese == Parliaments # 14
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard == dog # 3
                if OldGold == snails # 7
                if nextto(houses.index(Chesterfields), houses.index(fox)) # 11
                if nextto(houses.index(Kools), houses.index(horse)) # 12
                )

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def drinks_water():
    return zebra_puzzle()[0]

def owns_zebra():
    return zebra_puzzle()[1]