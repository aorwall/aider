def is_valid(isbn):
    # Remove hyphens from the ISBN
    isbn = isbn.replace('-', '')

    # Check if the length of the ISBN is 10 characters
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(10):
        # Multiply each digit by its weight in descending order
        try:
            total += int(isbn[i]) * (10 - i)
        except ValueError:
            return False

    # The check digit is 'X', which represents '10'
    if isbn[-1] == 'X':
        total += 10

    # If the sum modulo 11 equals 0, then it is a valid ISBN-10
    return total % 11 == 0
