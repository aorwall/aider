def is_armstrong_number(number):
    """
    Determines whether a given number is an Armstrong number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to a list of digits
    digits = [int(d) for d in str(number)]

    # Calculate the sum of the digits raised to the power of the number of digits
    armstrong_sum = sum(d ** len(digits) for d in digits)

    # Check if the sum is equal to the original number
    return armstrong_sum == number
