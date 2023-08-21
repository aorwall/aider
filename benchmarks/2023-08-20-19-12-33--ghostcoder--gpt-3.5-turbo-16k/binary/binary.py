def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)
    decimal = 0
    power = len(binary_string) - 1
    for digit in binary_string:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal