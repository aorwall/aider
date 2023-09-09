import itertools

def combinations(target, size, exclude=[]):
    """Return all valid combinations for a killer sudoku cage.

    Parameters:
    target (int): The target sum of the cage.
    size (int): The number of cells in the cage. 
    exclude (list, optional): Numbers already used in the cage/row/column.

    Returns:
    List of tuples containing valid combinations sorted in ascending order.
    """

    combinations = []

    # Generate all possible combinations
    for combo in itertools.combinations(range(1,10), size):
        if sum(combo) == target and not any(c in exclude for c in combo):
            combinations.append(tuple(sorted(combo)))

    return sorted(combinations)
