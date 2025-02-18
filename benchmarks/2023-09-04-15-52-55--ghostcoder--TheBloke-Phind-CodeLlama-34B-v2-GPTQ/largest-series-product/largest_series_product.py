def largest_product(series, size):
    # Check inputs
    if len(str(series)) < size:
        raise ValueError("span must be smaller than string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif not str(series).isdigit():
        raise ValueError("digits input must only contain digits")

    # Calculate products
    products = []
    for i in range(len(str(series)) - size + 1):
        substring = int(str(series)[i : i + size])
        products.append(prod([int(d) for d in str(substring)]))

    return max(products)

def prod(factors):
    result = factors[0]
    for f in factors[1:]:
        result *= f
    return result
