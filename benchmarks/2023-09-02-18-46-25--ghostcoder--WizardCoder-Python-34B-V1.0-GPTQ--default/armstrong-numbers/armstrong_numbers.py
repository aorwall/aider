def is_armstrong_number(number):
    """
    Determines if a given number is an Armstrong number.
    
    Args:
        number (int): The integer to check for Armstrongness.
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    # Convert the number to string to get its digits as a list of integers
    digits = [int(digit) for digit in str(number)]
    n = len(digits)

    # Calculate the sum of each digit raised to the power of n
    total = sum([num ** n for num in digits])

    return total == number
