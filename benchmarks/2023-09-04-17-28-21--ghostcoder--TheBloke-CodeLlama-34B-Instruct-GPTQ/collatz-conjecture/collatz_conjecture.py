def steps(number):
    """Return the number of steps required to reach 1.
    
    Args:
        number (int): A strictly positive integer.
        
    Returns:
        int: The number of steps required to reach 1.
        
    Raises:
        ValueError: If the given number is not strictly positive.
    """
    # Check if the given number is valid
    if number <= 0:
        raise ValueError("Only positive integers are allowed.")

    # Initialize variables
    count = 0
    current = number

    # Loop until we reach 1
    while current != 1:
        # Apply the Collatz algorithm
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1

        # Increment the step counter
        count += 1

    # Return the number of steps
    return count
