def is_valid(isbn):
    # Remove any dashes from the ISBN
    isbn = isbn.replace("-", "")

    # Check if the ISBN has the correct length
    if len(isbn) != 10:
        return False

    # Check if the last character is a valid check digit
    if isbn[-1] not in "0123456789X":
        return False

    # Calculate the sum of the products of each digit and its position
    total = 0
    for i, digit in enumerate(isbn):
        if digit == "X":
            digit = 10
        try:
            total += int(digit) * (10 - i)
        except ValueError:
            return False

    # Check if the total is divisible by 11
    return total % 11 == 0