def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    total = sum((10 - i) * (int(digit) if digit != 'X' else 10) for i, digit in enumerate(isbn))
    return total % 11 == 0