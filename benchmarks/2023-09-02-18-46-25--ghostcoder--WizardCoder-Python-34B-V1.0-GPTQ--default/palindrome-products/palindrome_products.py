def largest(min_factor=0, max_factor=10):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def get_factors(product):
        factors = []
        for i in range(min_factor, max_factor + 1):
            if product % i == 0:
                factors.append((i, product // i))
        return factors

    def check_range():
        if min_factor > max_factor:
            raise ValueError("min must be <= max")

    check_range()

    palindromes = [i * j for i in range(min_factor, max_factor + 1) for j in range(min_factor, max_factor + 1) if is_palindrome(i * j)]
    largest_palindrome = max(palindromes)
    smallest_palindrome = min(palindromes)

    return ((largest_palindrome, get_factors(largest_palindrome)), (smallest_palindrome, get_factors(smallest_palindrome)))


def smallest(min_factor=2, max_factor=9):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.
    
    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def get_factors(product):
        factors = []
        for i in range(min_factor, max_factor + 1):
            if product % i == 0:
                factors.append((i, product // i))
        return factors

    def check_range():
        if min_factor > max_factor or min_factor < 2:
            raise ValueError("min must be >= 2 and <= max")

    check_range()

    palindromes = [i * j for i in range(min_factor, max_factor + 1) for j in range(min_factor, max_factor + 1) if is_palindrome(i * j)]
    largest_palindrome = max(palindromes)
    smallest_palindrome = min(palindromes)

    return ((largest_palindrome, get_factors(largest_palindrome)), (smallest_palindrome, get_factors(smallest_palindrome)))