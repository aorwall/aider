from itertools import combinations as c
def combinations(target, size, exclude):
    """Generate all valid combinations for a given cage"""

    # Filter out excluded numbers and sort the remaining ones
    available_numbers = sorted([i for i in range(1, target+1) if i not in exclude])

    # Generate all possible combinations of 'size' distinct numbers that add up to 'target'
    result = [seq for seq in c(available_numbers, size) if sum(seq) == target]

    return sorted(result)
