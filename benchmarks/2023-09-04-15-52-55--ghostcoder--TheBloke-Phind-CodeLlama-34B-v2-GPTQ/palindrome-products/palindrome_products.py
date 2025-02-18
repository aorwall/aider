def largest(min_factor=0, max_factor=None):
    # Input validation: 'max_factor' must be greater than 'min_factor'.
    if max_factor < min_factor:
        raise ValueError("Max factor must be >= Min factor.")

    # Initialize maximum palindrome and its factors.
    max_palindrome = None
    max_factors = []

    for i in reversed(range(min_factor, max_factor+1)):
        for j in reversed(range(i, max_factor+1)):
            product = str(i * j)
            if product == product[::-1]:  # If the product is a palindrome.
                if max_palindrome is None or i*j > max_palindrome:
                    max_palindrome = i * j
                    max_factors = [(i, j)]

    return max_palindrome, max_factors


def smallest(min_factor=0, max_factor=None):
    # Input validation: 'max_factor' must be greater than 'min_factor'.
    if max_factor < min_factor:
        raise ValueError("Max factor must be >= Min factor.")

    # Initialize minimum palindrome and its factors.
    min_palindrome = float('inf')
    min_factors = []

    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            product = i * j
            product_str = str(product)
            if product_str == product_str[::-1] and product < min_palindrome:  # If the product is a smaller palindrome.
                min_palindrome = product
                min_factors = [(i, j)]

    return min_palindrome, min_factors