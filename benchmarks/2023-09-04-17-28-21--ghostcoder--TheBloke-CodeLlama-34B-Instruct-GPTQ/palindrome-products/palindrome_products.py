def largest(min_factor=1, max_factor=9):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Initialize variables
    palindrome = 0
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > palindrome:
                    palindrome = product
                    factors = [i, j]

    return palindrome, factors

def smallest(min_factor=1, max_factor=9):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # Initialize variables
    palindrome = 0
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product < palindrome or palindrome == 0:
                    palindrome = product
                    factors = [i, j]

    return palindrome, factors