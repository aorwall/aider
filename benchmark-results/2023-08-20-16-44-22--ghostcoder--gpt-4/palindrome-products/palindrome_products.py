def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    max_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1] and (max_palindrome is None or product >= max_palindrome):
                if max_palindrome is None or product > max_palindrome:
                    max_palindrome = product
                    factors = [(i, j)]
                elif product == max_palindrome:
                    factors.append((i, j))

    return (max_palindrome, factors) if max_palindrome is not None else (None, [])


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    min_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if str(product) == str(product)[::-1] and (min_palindrome is None or product <= min_palindrome):
                if min_palindrome is None or product < min_palindrome:
                    min_palindrome = product
                    factors = [(i, j)]
                elif product == min_palindrome:
                    factors.append((i, j))

    return (min_palindrome, factors) if min_palindrome is not None else (None, [])