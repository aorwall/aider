def square_root(number):
    """
    Calculate the square root of a natural number using the Babylonian method.
    :param number: The natural number to calculate the square root of.
    :return: The square root of the number.
    """
    # Initialize the guess for the square root
    guess = number / 2
    # Iterate until the difference between the guess and the actual value is less than 1
    while abs(guess * guess - number) >= 1:
        # Update the guess using the Babylonian method
        guess = (guess + number / guess) / 2
    return guess
