def rebase(input_base, digits, output_base):
    # Check if input_base and output_base are valid
    if input_base < 2 or output_base < 2:
        raise ValueError("Both input base and output base must be >= 2.")

    # Check if all digits are within range
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("All digits must satisfy 0 <= d < input base.")

    # Convert number from input base to decimal (base 10)
    num_decimal = 0
    power = len(digits) - 1
    for digit in digits:
        num_decimal += digit * (input_base ** power)
        power -= 1

    # Convert number from decimal (base 10) to output base
    result = []
    while num_decimal > 0:
        remainder = num_decimal % output_base
        num_decimal //= output_base
        result.append(remainder)

    return result[::-1]   # Reverse list to get correct order
