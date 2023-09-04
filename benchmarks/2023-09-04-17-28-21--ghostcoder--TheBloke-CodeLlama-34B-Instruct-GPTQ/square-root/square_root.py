def square_root(number):
    """
    Calculate the square root of a natural number using the Babylonian method.
    
    Args:
        number (int): The natural number to calculate the square root of.
        
    Returns:
        int: The calculated square root of the input number.
    """
    # Initialize the guess for the square root
    guess = number / 2

    # Iteratively improve the guess until it matches the expected precision
    while abs(guess ** 2 - number) >= 1:
        guess = (guess + number / guess) / 2

    return int(guess)
