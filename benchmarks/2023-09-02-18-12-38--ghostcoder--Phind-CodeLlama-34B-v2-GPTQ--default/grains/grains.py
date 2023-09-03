def square(number):
    """Return the number of grains on the given square"""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on the chessboard"""
    return sum(square(i) for i in range(1, 65))
