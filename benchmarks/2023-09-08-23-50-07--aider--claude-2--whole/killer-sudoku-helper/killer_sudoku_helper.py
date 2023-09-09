from itertools import permutations


def combinations(target, size, exclude):
    digits = [i for i in range(1, 10) if i not in exclude]
    
    combos = []
    for perm in permutations(digits, size):
        if sum(perm) == target:
            combos.append(list(perm))
    
    combos.sort()
    return combos
