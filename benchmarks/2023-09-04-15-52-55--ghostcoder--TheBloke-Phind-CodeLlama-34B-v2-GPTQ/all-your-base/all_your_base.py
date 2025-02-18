def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("Both bases have to be at least 2.")

    num_decimal = 0
    for digit in digits[::-1]:   # Reverse iterate over the digits
        num_decimal += digit * pow(input_base, digits.index(digit))  # Calculate the decimal equivalent

    if output_base == 10:   # If the output base is 10, we can directly return the decimal equivalent
        return [int(i) for i in str(num_decimal)]

    result = []  # Initialize an empty list for storing the digits in the new base
    while num_decimal > 0:
        result.append(num_decimal % output_base)
        num_decimal //= output_base

    # As we built up the result backwards, we need to reverse it now
    result.reverse()
    return result
