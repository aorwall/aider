import itertools
from itertools import combinations

def combinations(target, size, exclude):
    """Return a list of valid combinations for a given target sum, size, and excluded values."""
    # Generate all possible combinations of numbers up to 'size'
    candidates = [range(1, size + 1)] * size

    # Filter out combinations containing excluded values
    filtered_combinations = []
    for combination in itertools.product(*candidates):
        if set(combination) & set(exclude):
            continue

        # Check if the sum of the current combination matches the target
        if sum(combination) == target:
            filtered_combinations.append(sorted(combination))

    return sorted(filtered_combinations)
