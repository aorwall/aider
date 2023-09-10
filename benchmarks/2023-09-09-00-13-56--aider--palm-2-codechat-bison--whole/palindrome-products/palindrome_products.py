def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    # Check if the max_factor is less than the min_factor
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    # Find all palindromes in the given range
    palindromes = []
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)

    # Find the largest palindrome
    largest_palindrome = max(palindromes)

    # Find the factors of the largest palindrome
    factors = []
    for i in range(1, int(largest_palindrome ** 0.5) + 1):
        if largest_palindrome % i == 0:
            factors.append(i)
            factors.append(largest_palindrome // i)

    # Return the largest palindrome and its factors
    return (largest_palindrome, factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    # Check if the max_factor is less than the min_factor
    if max