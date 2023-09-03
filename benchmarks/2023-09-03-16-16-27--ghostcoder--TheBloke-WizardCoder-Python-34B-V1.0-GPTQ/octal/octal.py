def parse_octal(digits):
    if digits == '':
        raise ValueError('Empty string is not valid')
    elif any(c not in '01234567' for c in digits):
        raise ValueError('Invalid character found')
    else:
        return int(digits, base=8)
