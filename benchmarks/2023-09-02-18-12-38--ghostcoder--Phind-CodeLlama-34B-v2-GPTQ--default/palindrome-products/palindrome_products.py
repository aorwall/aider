def largest(min_factor=0, max_factor=1):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Check if input parameters are valid
    if max_factor < min_factor:
        raise ValueError("max must be >= min")

    # Initialize variables
    palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = str(i * j)
            # If product is a palindrome and it's greater than current maximum
            if product == product[::-1] and (not palindrome or int(product) > palindrome):
                palindrome = int(product)
                factors = [(i, j)]
            elif product == product[::-1] and int(product) == palindrome:
                factors.append((i, j))

    return palindrome, factors


def smallest(min_factor=0, max_factor=1):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Check if input parameters are valid
    if max_factor < min_factor:
        raise ValueError("max must be >= min")

    # Initialize variables
    palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = str(i * j)
            # If product is a palindrome and it's smaller than current minimum
            if product == product[::-1] and (not palindrome or int(product) < palindrome):
                palindrome = int(product)
                factors = [(i, j)]
            elif product == product[::-1] and int(product) == palindrome:
                factors.append((i, j))

    return palindrome, factors