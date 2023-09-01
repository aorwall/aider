def parse_octal(digits):
    result = 0
    for i, digit in enumerate(digits):
        result += (ord(digit) - ord('0')) * 8 ** i
    return result