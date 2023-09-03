def parse_octal(digits):
    decimal = 0
    for i, digit in enumerate(digits):
        decimal += int(digit) * 8 ** i
    return decimal
