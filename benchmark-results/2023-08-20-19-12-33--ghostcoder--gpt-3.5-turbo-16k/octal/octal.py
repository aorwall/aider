def parse_octal(digits):
    if not all(digit.isdigit() and int(digit) < 8 for digit in digits):
        raise ValueError("Invalid octal input")
    decimal = 0
    power = 0
    for digit in reversed(digits):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal