from itertools import combinations

def get_valid_combinations(target, size, exclude):
    valid_combinations = []
    for combination in combinations(range(1, 10), size):
        if sum(combination) == target and not any(num in exclude for num in combination):
            valid_combinations.append(list(combination))
    return sorted(valid_combinations)
