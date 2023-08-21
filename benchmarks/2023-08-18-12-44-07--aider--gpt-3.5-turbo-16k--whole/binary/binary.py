def parse_binary(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        if digit == '0' or digit == '1':
            decimal += int(digit) * (2 ** power)
            power -= 1
        else:
            raise ValueError("Invalid binary literal: " + binary_string)

    return decimal
