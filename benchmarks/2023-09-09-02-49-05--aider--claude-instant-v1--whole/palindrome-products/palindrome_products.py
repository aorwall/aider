from math import sqrt
from itertools import product

def largest(max_factor, min_factor=0):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param max_factor: int
    :param min_factor: int, default 0
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindromes = filter(lambda x: str(x) == str(x)[::-1], map(lambda x: x[0]*x[1], product(range(min_factor, max_factor+1), repeat=2)))
    return max(palindromes), tuple(map(list, product(range(min_factor, max_factor+1), repeat=2))[palindromes.index(max(palindromes))])

def smallest(min_factor=0, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindromes = filter(lambda x: str(x) == str(x)[::-1], map(lambda x: x[0]*x[1], product(range(min_factor, max_factor+1), repeat=2)))
    return min(palindromes), tuple(map(list, product(range(min_factor, max_factor+1), repeat=2))[palindromes.index(min(palindromes))])
