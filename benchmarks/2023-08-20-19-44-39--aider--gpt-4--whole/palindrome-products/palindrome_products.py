def is_palindrome(n):
    """Check if a number is a palindrome.

    :param n: int
    :return: bool
    """
    return str(n) == str(n)[::-1]


def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_palindrome = 0
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
                    factors = [(i, j)]
                elif product == max_palindrome:
                    factors.append((i, j))

    return (None, []) if max_palindrome == 0 else (max_palindrome, factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    min_palindrome = float('inf')
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if product < min_palindrome:
                    min_palindrome = product
                    factors = [(i, j)]
                elif product == min_palindrome:
                    factors.append((i, j))

    return (None, []) if min_palindrome == float('inf') else (min_palindrome, factors)
