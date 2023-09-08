def combinations(target, size, exclude):
    """
    Returns a list of valid combinations for a given cage sum and size, excluding the specified digits.

    Args:
        target (int): The target cage sum.
        size (int): The size of the cage.
        exclude (list): The digits to exclude from the combinations.

    Returns:
        list: A list of valid combinations.
    """

    def is_valid_combination(combination):
        return sum(combination) == target and len(set(combination)) == size

    def generate_combinations(current, remaining_size, current_sum):
        if remaining_size == 0:
            if is_valid_combination(current):
                yield current
        else:
            for digit in range(1, 10):
                if digit not in exclude:
                    new_current = current + [digit]
                    new_current_sum = current_sum + digit
                    yield from generate_combinations(new_current, remaining_size - 1, new_current_sum)

    return sorted(list(generate_combinations([], size, 0)))