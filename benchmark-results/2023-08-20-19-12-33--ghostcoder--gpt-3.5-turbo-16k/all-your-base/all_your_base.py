def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if len(digits) == 0:
        return [0]

    decimal = 0
    for digit in digits:
        decimal = decimal * input_base + digit

    result = []
    while decimal > 0:
        result.append(decimal % output_base)
        decimal //= output_base

    return result[::-1]