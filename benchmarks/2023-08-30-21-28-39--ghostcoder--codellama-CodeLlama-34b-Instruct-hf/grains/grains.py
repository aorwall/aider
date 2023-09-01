def square(number):
    """
    Calculates the number of grains of wheat on a given square of a chessboard.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """
    Calculates the total number of grains of wheat on a chessboard.
    """
    return sum(square(i) for i in range(1, 65))
