import math

def largest(max_factor, min_factor=0):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("max must be >= min")
    
    products = []
    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            product = x * y
            if str(product) == str(product)[::-1]:
                products.append((product, [x, y]))
    
    if products:
        return max(products)
    else:
        return (None, [])


def smallest(max_factor, min_factor=0):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    
    if max_factor < min_factor:
        raise ValueError("max must be >= min")

    products = []
    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            product = x * y
            if str(product) == str(product)[::-1]:
                products.append((product, [x, y]))
    
    if products:
        return min(products)
    else:
        return (None, [])
