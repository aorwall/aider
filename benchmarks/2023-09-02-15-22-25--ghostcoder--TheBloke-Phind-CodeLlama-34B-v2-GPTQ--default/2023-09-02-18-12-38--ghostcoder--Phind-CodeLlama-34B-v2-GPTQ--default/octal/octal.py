def parse_octal(digits):
    """Convert an octal number, represented as a string, to its decimal equivalent."""

    if not digits or int(digits) == 0:
        return 0

    decimal = 0
    power = len(digits) - 1

    for digit in reversed(digits):
        decimal += int(digit) * (8 ** power)
        power -= 1

    return decimal
