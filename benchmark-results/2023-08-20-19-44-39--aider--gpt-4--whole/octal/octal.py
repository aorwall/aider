def parse_octal(digits):
    if any(int(digit) > 7 for digit in digits):
        raise ValueError("Invalid octal number")
    try:
        return sum(int(digit) * 8 ** index for index, digit in enumerate(reversed(digits)))
    except ValueError:
        return 0
