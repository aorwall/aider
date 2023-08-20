def combinations(target, size, exclude):
    # Base cases
    if size == 0:
        return [[]] if target == 0 else []
    if size < 0 or target <= 0:
        return []

    result = []
    for i in range(1, 10):
        if i not in exclude:
            # Recursively find combinations that add up to target - i
            for combo in combinations(target - i, size - 1, exclude + [i]):
                # Sort each combination before appending it to the result list
                result.append(sorted([i] + combo))

    # Remove duplicates from the result list before returning it
    return sorted(list(set(tuple(comb) for comb in result)))