def parse_octal(digits):
    if not all(char in '01234567' for char in digits):
        raise ValueError("Invalid octal number")

    decimal = 0
    for i, digit in enumerate(reversed(digits)):
        decimal += int(digit) * (8 ** i)

    return decimal