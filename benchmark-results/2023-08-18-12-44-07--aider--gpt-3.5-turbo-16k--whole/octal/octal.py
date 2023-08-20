def parse_octal(digits):
    decimal = 0
    power = len(digits) - 1

    for digit in digits:
        if not digit.isdigit() or int(digit) >= 8:
            raise ValueError("Invalid octal digit")
        decimal += int(digit) * (8 ** power)
        power -= 1

    return decimal
