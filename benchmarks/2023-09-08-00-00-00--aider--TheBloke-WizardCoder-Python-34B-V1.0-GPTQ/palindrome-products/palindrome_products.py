def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    def is_palindrome(number):
        return str(number) == str(number)[::-1]

    def palindrome_products(min_factor, max_factor):
        palindromes = []
        for i in range(min_factor, max_factor + 1):
            for j in range(i, max_factor + 1):
                product = i * j
                if is_palindrome(product):
                    palindromes.append((product, (i, j)))
        return palindromes

    palindromes = palindrome_products(min_factor, max_factor)
    if not palindromes:
        raise ValueError("No palindromes found in the given range")

    largest_palindrome = max(palindromes, key=lambda x: x[0])
    return largest_palindrome

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    def is_palindrome(number):
        return str(number) == str(number)[::-1]

    def palindrome_products(min_factor, max_factor):
        palindromes = []
        for i in range(min_factor, max_factor + 1):
            for j in range(i, max_factor + 1):
                product = i * j
                if is_palindrome(product):
                    palindromes.append((product, (i, j)))
        return palindromes

    palindromes = palindrome_products(min_factor, max_factor)
    if not palindromes:
        raise ValueError("No palindromes found in the given range")

    smallest_palindrome = min(palindromes, key=lambda x: x[0])
    return smallest_palindrome
