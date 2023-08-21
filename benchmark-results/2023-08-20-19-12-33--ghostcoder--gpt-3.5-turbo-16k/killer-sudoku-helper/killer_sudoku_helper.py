def combinations(target, size, exclude):
    """
    Returns a list of all valid combinations of digits that add up to the target sum,
    with the given size, and excluding the digits in the exclude list.
    """
    def backtrack(remaining, current_combination, start):
        if remaining == 0 and len(current_combination) == size:
            combinations.append(current_combination.copy())
            return
        if remaining < 0 or len(current_combination) == size:
            return
        for i in range(start, 10):
            if i not in exclude:
                current_combination.append(i)
                backtrack(remaining - i, current_combination, i + 1)
                current_combination.pop()

    combinations = []
    backtrack(target, [], 1)
    return sorted(combinations)