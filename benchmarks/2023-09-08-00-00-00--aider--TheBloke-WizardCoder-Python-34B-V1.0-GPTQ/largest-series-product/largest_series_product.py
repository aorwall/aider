def largest_product(series, span):
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    if span > len(series):
        raise ValueError("span must be smaller than string length")
    if span < 0:
        raise ValueError("span must not be negative")
    
    max_product = 0
    for i in range(len(series) - span + 1):
        product = 1
        for j in range(span):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product
