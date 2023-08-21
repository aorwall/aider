def largest_product(series, size):
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if size == 0:
        return 1
    return max(product_of_digits(series[i:i+size]) for i in range(len(series) - size + 1))

def product_of_digits(digits):
    product = 1
    for digit in digits:
        product *= int(digit)
    return product
