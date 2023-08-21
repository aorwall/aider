def is_valid(isbn):
    # Remove any hyphens from the ISBN string
    isbn = isbn.replace('-', '')

    # Check if the ISBN is of valid length
    if len(isbn) != 10:
        return False

    # Check if the last character is 'X' and replace it with '10'
    if isbn[-1] == 'X':
        isbn = isbn[:-1] + '10'

    # Check if all characters are digits or 'X'
    if not isbn[:-1].isdigit() or isbn[-1] not in '0123456789X':
        return False

    # Calculate the sum of the products of each digit and its position
    total = sum(int(digit) * (10 - index) for index, digit in enumerate(isbn))

    # Check if the total is divisible by 11
    return total % 11 == 0
