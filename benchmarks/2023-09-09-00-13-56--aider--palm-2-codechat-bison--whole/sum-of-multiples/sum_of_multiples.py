def sum_of_multiples(limit, multiples):
    """
    This function calculates the sum of the multiples of the given numbers
    that are less than the given limit.

    Args:
        limit (int): The maximum number to consider.
        multiples (list): A list of numbers to find the multiples of.

    Returns:
        int: The sum of the multiples of the given numbers that are less than the given limit.
    """

    # Check if the limit is less than or equal to 0.
    if limit <= 0:
        return 0

    # Check if the multiples list is empty.
    if not multiples:
        return 0

    # Check if any of the numbers in the multiples list are not positive.
    for multiple in multiples:
        if multiple < 1:
            raise ValueError("All numbers in the multiples list must be positive.")

    # Check if the multiples list contains a number that is equal to 0.
    if 0 in multiples:
        raise ValueError("The multiples list cannot contain the number 0.")

    # Calculate the sum of the multiples.
    sum_of_multiples = 0
    for multiple in multiples:
        for i in range(1, limit // multiple +