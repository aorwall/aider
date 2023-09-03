def square(number):
    """
    Returns the number of grains on a specific square.
    """
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """
    Returns the total number of grains on the chessboard.
    """
    return sum(square(number) for number in range(1, 65))
