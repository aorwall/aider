def rebase(input_base, digits, output_base):
    """Converts a number from any base to any base."""
    # Check if input_base and output_base are valid.
    if input_base <= 0 or output_base <= 0:
        raise ValueError("Input and Output bases must be greater than zero.")

    # Convert list of digits to integer value using input_base.
    num = sum([digits[i] * input_base ** (len(digits)-1 - i) for i in range(len(digits))])

    # Initialize result list.
    res = []
    while num > 0:
        res.append(num % output_base)
        num //= output_base

    return res[::-1]
