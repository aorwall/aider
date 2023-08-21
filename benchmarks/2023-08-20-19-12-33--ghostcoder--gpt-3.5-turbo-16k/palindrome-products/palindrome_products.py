def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    largest_palindrome = None
    factors = []

    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if is_palindrome(product):
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = [(j, i)]
                elif product == largest_palindrome:
                    factors.append((j, i))

    return largest_palindrome, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    smallest_palindrome = None
    factors = []

    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            if is_palindrome(product):
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = [(i, j)]
                elif product == smallest_palindrome:
                    factors.append((i, j))

    return smallest_palindrome, factors