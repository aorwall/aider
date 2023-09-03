def largest_product(series, size):
    # Check for valid inputs
    if len(series) < size:
        raise ValueError("span must be smaller than string length")

    if size <= 0:
        raise ValueError("span must not be negative")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    product = None
    for i in range(len(series)-size+1):
        substring = series[i:i+size]
        current_product = 1
        for digit in substring:
            current_product *= int(digit)
        if product is None or current_product > product:
            product = current_product

    return product
