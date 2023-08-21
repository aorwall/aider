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

    palindromes = []
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
                factors.append((i, j))

    if not palindromes:
        return None, []

    max_palindrome = max(palindromes)
    max_factors = [f for p, f in zip(palindromes, factors) if p == max_palindrome]

    return max_palindrome, max_factors


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

    palindromes = []
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:
                palindromes.append(product)
                factors.append((i, j))

    if not palindromes:
        return None, []

    min_palindrome = min(palindromes)
    min_factors = [f for p, f in zip(palindromes, factors) if p == min_palindrome]

    return min_palindrome, min_factors
