def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    decimal = 0
    for d in digits:
        if d >= input_base:
            raise ValueError("digit must be less than input base")
        decimal = decimal * input_base + d

    result = []
    while decimal > 0:
        result.append(int(decimal % output_base))
        decimal //= output_base

    result.reverse()

    if len(result) == 0:
        result.append(0)

    return result
