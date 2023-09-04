from itertools import combinations

def combinations(target, size, exclude=[]):
    return list(filter(lambda x: sum(x) == target and len(set(x)) == size and set(x).isdisjoint(exclude), combinations([i+1 for i in range(size*2)], size)))

def combinations(target, size, exclude):
    return list(filter(lambda x: sum(x) == target and len(set(x)) == size and set(x).isdisjoint(exclude), combinations([i+1 for i in range(size*2)], size)))
