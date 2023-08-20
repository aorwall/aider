def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if 'X' in isbn[:-1] or isbn.count('X') > 1:
        return False
    if not all(char.isdigit() or char == 'X' for char in isbn):
        return False
    isbn = isbn.replace('X', '10')
    total = sum(int(digit) * weight for digit, weight in zip(isbn, range(10, 0, -1)))
    return total % 11 == 0
