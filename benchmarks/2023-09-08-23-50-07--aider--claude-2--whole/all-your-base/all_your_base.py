def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    total = 0
    for i, digit in enumerate(digits[::-1]):
        if digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        total += digit * (input_base ** i)

    output_digits = []
    while total > 0:
        digit = total % output_base
        total //= output_base
        output_digits.append(digit)

    if not digits and output_base != 10:
        output_digits = [0]

    return output_digits[::-1]
