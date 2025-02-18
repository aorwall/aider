def is_valid(isbn):
    # Remove dashes from the input
    isbn = isbn.replace('-', '')

    # If the length of the input is not 10 or 13, return False
    if len(isbn) != 10 and len(isbn) != 13:
        return False

    # Check if the last character is 'X', convert it to 10 if so
    if len(isbn) == 10 and isbn[-1].upper() == 'X':
        isbn = isbn[:-1] + '10'

    # Calculate the checksum
    try:
        checksum = sum((i+1)*int(digit) for i, digit in enumerate(isbn)) % 11
    except ValueError:
        return False

    # The ISBN is valid iff the checksum equals 0
    return checksum == 0
