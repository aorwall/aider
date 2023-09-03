def steps(number):
    """Calculate the number of steps required to reach 1 using the Collatz Conjecture.
    
    Args:
        number (int): A strictly positive integer.
        
    Returns:
        int: Number of steps required to reach 1.
        
    Raises:
        ValueError: If the input number is zero or a negative integer.
    """
    # Check for invalid inputs
    if number <= 0:
        raise ValueError("Only positive integers are allowed.")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1

    return count
