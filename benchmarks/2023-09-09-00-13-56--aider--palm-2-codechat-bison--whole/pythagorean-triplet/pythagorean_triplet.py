def triplets_with_sum(number):
    """
    Find all Pythagorean triplets for which `a + b + c = N`.

    For example, with N = 1000, there is exactly one Pythagorean triplet for which `a + b + c = 1000`: `{200, 375, 425}`.

    Args:
        number: The sum of the Pythagorean triplet.

    Returns:
        A list of lists of the Pythagorean triplets.
    """

    # Find all possible values for `a`.
    a_values = []
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1):
            a_values.append(i * i + j * j)

    # Find all possible values for `b`.
    b_values = []
    for a_value in a_values:
        for c_value in a_values:
            if a_value + c_value == number:
                b_value = number - a_value - c_value
                b_values.append(b_value)

    # Return all possible Pythagorean triplets.
    return [[a, b, c] for a, b, c in zip(a_values, b_values, a_values)]
