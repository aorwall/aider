def square_of_sum(number):
    """
    Finds the square of the sum of the first `number` natural numbers.

    Args:
        number: The number of natural numbers to sum.

    Returns:
        The square of the sum of the first `number` natural numbers.
    """

    sum_of_numbers = sum(range(1, number + 1))
    return sum_of_numbers ** 2


def sum_of_squares(number):
    """
    Finds the sum of the squares of the first `number` natural numbers.

    Args:
        number: The number of natural numbers to sum.

    Returns:
        The sum of the squares of the first `number` natural numbers.
    """

    sum_of_squares = 0
    for i in range(1, number + 1):
        sum_of_squares += i ** 2

    return sum_of_squares


def difference_of_squares(number):
    """
    Finds the difference between the square of the sum and the sum of the squares of the first `number` natural numbers.

    Args:
        number: The number of natural numbers to sum.

    Returns:
        The difference between the square of the sum and the sum of the squares of the first `number` natural numbers.
    """

    square_of_sum = square_of_sum(number)
    sum_of_squares = sum_of_squares(number)

    return square_of_sum - sum_of_squares
