import itertools

def zebra_puzzle():
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(h1=ivory, h2=green) # 6
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                if Englishman == red # 2
                if Norwegian == 1 # 10
                if nextto(h1=Norwegian, h2=blue) # 15
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee == green # 4
                if Ukrainian == tea # 5
                if milk == 3 # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools == yellow # 8
                if LuckyStrike == oj # 13
                if Japanese == Parliaments # 14
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard == dog # 3
                if OldGold == snails # 7
                if nextto(h1=Chesterfields, h2=fox) # 11
                if nextto(h1=Kools, h2=horse) # 12
                )

def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def drinks_water():
    _, water = zebra_puzzle()
    return "The resident of house number {} drinks water.".format(water)

def owns_zebra():
    zebra, _ = zebra_puzzle()
    return "The resident of house number {} owns the zebra.".format(zebra)
