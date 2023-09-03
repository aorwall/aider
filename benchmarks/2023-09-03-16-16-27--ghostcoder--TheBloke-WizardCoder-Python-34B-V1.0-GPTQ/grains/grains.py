def square(number):
    """Calculate the number of grains of wheat on a single square.
    
    Args:
        number (int): A positive integer representing the square on the chessboard.
    
    Returns:
        int: The number of grains of wheat on that square.
    
    Raises:
        ValueError: If the square is less than 1 or greater than 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """Calculate the total number of grains of wheat on all squares of the chessboard."""
    return 2**64 - 1
