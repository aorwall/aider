def parse_binary(binary_string):
    # Check if string contains only 0s and 1s
    if not set(binary_string).issubset('01'):
        raise ValueError("Invalid binary literal")

    decimal = 0
    for digit in reversed(binary_string):
        decimal += int(digit) * (2 ** (len(binary_string) - 1 - binary_string.index(digit)))

    return decimal
