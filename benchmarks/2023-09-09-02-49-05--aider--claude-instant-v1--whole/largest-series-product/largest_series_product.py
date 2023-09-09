import math

def largest_product(series, size):

    if size > len(series) or size < 1:
        if size > len(series):
            raise ValueError("span must be smaller than string length")
        elif size < 1:
            raise ValueError("span must not be negative")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    products = []

    for i in range(len(series)-size+1):
        substring = series[i:i+size]
        product = 1
        for char in substring:
            product *= int(char)
        products.append(product)

    return max(products)
