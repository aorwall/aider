def largest_product(series, size):
    """Return the largest product of consecutive digits of given length.
    
    Args:
        series: A string containing a series of digits.
        size: An integer indicating the desired length of consecutive digits.
    
    Returns:
        An integer representing the largest product of consecutive digits.
    
    Raises:
        ValueError: If size is larger than the length of series or less than 0.
    
    Examples:
        >>> largest_product('12345', 2)
        12
        >>> largest_product('12345', 3)
        60
        >>> largest_product('12345', 4)
        240
        >>> largest_product('12345', 5)
        1200
        >>> largest_product('12345', 6)
        Traceback (most recent call last):
            ...
        ValueError: span must be smaller than string length
        >>> largest_product('abcd', 2)
        Traceback (most recent call last):
            ...
        ValueError: digits input must only contain digits
        >>> largest_product('12345', -1)
        Traceback (most recent call last):
            ...
        ValueError: span must not be negative
    """
    # Check if size is valid
    if size > len(series) or size < 0:
        raise ValueError("span must be smaller than string length")

    # Initialize variables
    max_product = 0
    current_product = 1
    start_index = 0

    # Iterate over each digit in the series
    for i, digit in enumerate(series):
        # Check if digit is a number
        if not digit.isdigit():
            raise ValueError("digits input must only contain digits")

        # Calculate the product of consecutive digits
        current_product *= int(digit)

        # Check if the current product is greater than the maximum product
        if current_product > max_product:
            max_product = current_product

        # Check if the end of the series has been reached
        if i == len(series) - 1:
            break

        # Check if the window size has been exceeded
        if i - start_index + 1 == size:
            # Calculate the product of the previous window
            prev_window_product = 1
            for j in range(start_index, i):
                prev_window_product *= int(series[j])

            # Update the starting index
            start_index += 1

            # Divide the current product by the previous window product
            current_product //= prev_window_product

    return max_product
