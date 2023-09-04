def largest_product(series, size):
    # Check if inputs are valid
    if not isinstance(series, str) or not series.isdigit() or len(series) < size:
        raise ValueError("Invalid input provided.")

    max_product = 0

    for i in range(len(series) - size + 1):
        current_product = int(series[i])

        for j in range(i+1, i+size):
            current_product *= int(series[j])

        if current_product > max_product:
            max_product = current_product

    return max_product
