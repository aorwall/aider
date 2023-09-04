import math
from typing import Tuple, Iterable

def is_palindrome(number: str) -> bool:
    """Check if a given number is a palindrome."""
    return number == number[::-1]

def get_divisors(number: int) -> Iterable:
    """Get all divisors for a given number."""
    upper = int(math.sqrt(number)) + 1

    # Check for small primes first
    for i in range(2, 11):
        if number % i == 0:
            yield i
            yield number // i

    # Check odd numbers up to sqrt(n)
    for i in range(3, upper, 2):
        if number % i == 0:
            yield i
            yield number // i

def largest(min_factor: int = 0, max_factor: int = 1000) -> Tuple[int, Iterable]:
    """Given a range of numbers, find the largest palindromes which are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int with a default value of 1000
    :return: tuple of (palindrome, iterable).
           Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    def check_range(i, j):
        if i * j >= min_factor and i * j <= max_factor:
            if is_palindrome(str(i * j)):
                return i * j, (i, j)

        for i in reversed(range(2, max_factor + 1)):
            for j in get_divisors(i):
                result = check_range(i, j)
                if result:
                    return result

    return None, ()

    return check_range(max_factor, max_factor - 1)[0], check_range(max_factor, max_factor - 1)[1]

def smallest(min_factor: int = 0, max_factor: int = 1000) -> Tuple[int, Iterable]:
    """Given a range of numbers, find the smallest palindromes which are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int with a default value of 1000
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    def check_range(i, j):
        if i * j >= min_factor and i * j <= max_factor:
            if is_palindrome(str(i * j)):
                return i * j, (i, j)

        for i in range(min_factor, max_factor + 1):
            for j in get_divisors(i):
                result = check_range(i, j)
                if result:
                    return result

    return check_range(min_factor, min_factor + 1)[0], check_range(min_factor, min_factor + 1)[1]

    return smallest(min_factor, max_factor - 1)[0], smallest(min_factor, max_factor - 1)[1]