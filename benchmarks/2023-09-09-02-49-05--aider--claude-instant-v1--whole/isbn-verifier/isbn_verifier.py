import re

def is_valid(isbn):
    isbn = re.sub('[-]', '', isbn)
    if not isbn.isdigit() and len(isbn) != 10:
        return False

    total = 0
    isbn_numbers = []
    for char in isbn:
        if char.isdigit() or char == 'X':
            isbn_numbers.append(char)

    if len(isbn_numbers) != 10:
        return False

    for i, digit in enumerate(isbn_numbers):
        if digit == 'X':
            digit = 10
        else: 
            digit = int(digit)
        total += (digit * (10-i))

    check = total % 11
    if check == 0:
        check = '0'
    elif check == 1:
        check = 'X'

    return isbn_numbers[-1] == check
