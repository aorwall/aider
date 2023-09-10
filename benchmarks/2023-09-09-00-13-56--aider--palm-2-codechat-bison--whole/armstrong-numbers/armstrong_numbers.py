def is_armstrong_number(number):
    """
    Returns True if the given number is an Armstrong number.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

    Args:
        number: The number to check.

    Returns:
        True if the number is an Armstrong number, False otherwise.
    """

    # Get the number of digits in the given number.
    num_digits = len(str(number))

    # Calculate the sum of the digits of the given number, each raised to the power of the number of digits.
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit) ** num_digits

    # Return True if the sum of the digits is equal to the given number.
    return number == sum_of_digits
