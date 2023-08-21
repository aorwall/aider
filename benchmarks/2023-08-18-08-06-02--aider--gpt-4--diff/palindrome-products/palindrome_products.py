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

    palindromes = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
                if product not in palindromes:
                    palindromes[product] = [[i, j]]
                else:
                    palindromes[product].append([i, j])

    if palindromes:
        largest_palindrome = max(palindromes.keys())
        return largest_palindrome, palindromes[largest_palindrome]
    else:
        return None, []


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

    palindromes = {}
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1]:  # Check if the product is a palindrome
                if product not in palindromes:
                    palindromes[product] = [[i, j]]
                else:
                    palindromes[product].append([i, j])

    if palindromes:
        smallest_palindrome = min(palindromes.keys())
        return smallest_palindrome, palindromes[smallest_palindrome]
    else:
        return None, []
