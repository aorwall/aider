from collections import Counter
from itertools import permutations

def can_chain(dominoes):
    if len(dominoes) < 2:
        return False

    # Count the occurrences of each number on both sides of the dominoes
    counts = Counter()
    for d in dominoes:
        counts[(min(d), max(d))] += 1

    # Check if it's possible to create a loop by trying all possibilities
    for perm in permutations(dominoes):
        if check_loop((perm, counts)):
            return True

    return False

def check_loop(data):
    chain, counts = data
    prev_end = None

    for d in chain:
        start, end = min(d), max(d)
        if prev_end is not None and prev_end != start:
            return False

        if counts[(start, end)] > 0:
            counts[(start, end)] -= 1
        else:
            return False

        prev_end = end

    return True
