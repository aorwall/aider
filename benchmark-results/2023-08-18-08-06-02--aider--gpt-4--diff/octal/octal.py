def parse_octal(digits):
    if not digits.isdigit() or any(char in '89' for char in digits):
        raise ValueError("Invalid octal number")
    digits = digits[::-1]
    result = 0
    for i, digit in enumerate(digits):
        result += int(digit) * (8 ** i)
    return result
