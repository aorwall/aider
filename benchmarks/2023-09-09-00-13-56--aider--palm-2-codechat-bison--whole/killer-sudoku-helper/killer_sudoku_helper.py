def combinations(target, size, exclude):
    """
    Returns a list of all possible combinations of the given size that add up to the target.

    Args:
        target: The target number to add up to.
        size: The size of the combinations.
        exclude: A list of numbers that should not be included in the combinations.

    Returns:
        A list of all possible combinations of the given size that add up to the target.
    """

    # Initialize the list of combinations.
    combinations = []

    # Iterate over all possible combinations of the given size.
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            for k in range(1, size + 1):
                if i + j + k == target and i not in exclude and j not in exclude and k not in exclude:
                    combinations.append([i, j, k])

    # Return the list of combinations.
    return combinations

