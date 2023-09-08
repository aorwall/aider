def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)

    decimal = 0
    for i, digit in enumerate(reversed(binary_string)):
        decimal += int(digit) * 2**i

    return decimal
