def parse_octal(digits):
    if not set(digits).issubset('01234567'):
        raise ValueError("Invalid character")

    try:
        num = int(digits, 8)
    except ValueError:
        num = 0
    return num
