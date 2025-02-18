def rebase(input_base, digits, output_base):
    """Rebase given digits from input base to output base."""
    # Check validity of input and output bases.
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Convert input digits from arbitrary base to integer.
    num = 0
    for i, digit in enumerate(digits):
        if not (0 <= digit < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
        num += digit * input_base ** i

    # Convert integer to digits in output base.
    if num == 0:
        return [0]
    res = []
    while num > 0:
        num, rem = divmod(num, output_base)
        res.append(rem)
    return res[::-1]
