def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindrome which
    is a product of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Check if the min_factor is less than the max_factor
    if min_factor < max_factor:
        raise ValueError("min must be <= max")

    # Initialize the largest palindrome and its factors
    largest_palindrome = 0
    largest_factors = []

    # Iterate over the range of numbers
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            # Check if the product is a palindrome
            if str(product) == str(product)[::-1]:
                # If the product is larger than the current largest palindrome, update the largest palindrome and its factors
                if product > largest_palindrome:
                    largest_palindrome = product
                    largest_factors = [i, j]

    return (largest_palindrome, largest_factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindrome which
    is a product of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Check if the min_factor is less than the max_factor
    if min_factor < max_factor:
        raise ValueError("min must be <= max")

    # Initialize the smallest palindrome and its factors
    smallest_palindrome = 0
    smallest_factors = []

    # Iterate over the range of numbers
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            # Check if the product is a palindrome
            if str(product) == str(product)[::-1]:
                # If the product is smaller than the current smallest palindrome, update the smallest palindrome and its factors
                if product < smallest_palindrome or smallest_palindrome == 0:
                    smallest_palindrome = product
                    smallest_factors = [i, j]

    return (smallest_palindrome, smallest_factors)
