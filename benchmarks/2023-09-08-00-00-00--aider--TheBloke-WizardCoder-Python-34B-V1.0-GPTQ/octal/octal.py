def parse_octal(digits):
    decimal = 0
    for i, digit in enumerate(reversed(digits)):
        if '0' <= digit <= '7':
            decimal += int(digit) * (8 ** i)
        else:
            raise ValueError("Invalid octal digit: {}".format(digit))
    return decimal
