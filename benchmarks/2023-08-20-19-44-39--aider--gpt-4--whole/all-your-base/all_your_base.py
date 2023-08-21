def rebase(input_base, digits, output_base):
    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert the input digits to base 10
    number_in_base_10 = sum(d * (input_base ** i) for i, d in enumerate(reversed(digits)))

    # Convert the number in base 10 to the output base
    output_digits = []
    while number_in_base_10 > 0:
        number_in_base_10, digit = divmod(number_in_base_10, output_base)
        output_digits.append(digit)
    return output_digits[::-1] if output_digits else [0]
