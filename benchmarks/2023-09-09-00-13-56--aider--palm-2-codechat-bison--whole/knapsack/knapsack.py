def maximum_value(maximum_weight, items):
    """
    This function returns the maximum value that can be
    obtained by taking a subset of the items in the list
    such that the total weight of the subset does not
    exceed the maximum weight.

    Args:
        maximum_weight: The maximum weight that the knapsack
            can hold.
        items: A list of items, where each item is a
            dictionary with the following keys:
                - weight: The weight of the item.
                - value: The value of the item.

    Returns:
        The maximum value that can be obtained by taking a
        subset of the items in the list such that the total
        weight of the subset does not exceed the maximum
        weight.
    """

    # Initialize the table of values.
    table = [[0 for _ in range(maximum_weight + 1)] for _ in range(len(items) + 1)]

    # Populate the table.
    for i in range(1, len(items) + 1):
        for j in range(1, maximum_weight + 1):
            if items[i - 1]["weight"] <= j:
                table[i][j] = max(
                    table[i - 1][j],
                    table[i - 1][j - items[i - 1]["weight"]] + items[i - 1]["value"],
                )
            else:
                table[i][j] = table[i - 1][j]

    # Return the maximum value.
    return table[-1][-1]
