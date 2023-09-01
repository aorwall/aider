def is_valid(isbn):
    # Check if the input is a valid ISBN
    if not isbn.isdigit():
        return False

    # Check if the input is a valid ISBN-10
    if len(isbn) == 10:
        # Calculate the check digit
        check_digit = 0
        for i in range(9):
            check_digit += int(isbn[i]) * (10 - i)
        check_digit %= 11

        # Check if the check digit is valid
        if check_digit != int(isbn[9]):
            return False

    # Check if the input is a valid ISBN-13
    elif len(isbn) == 13:
        # Calculate the check digit
        check_digit = 0
        for i in range(12):
            check_digit += int(isbn[i]) * (13 - i)
        check_digit %= 11

        # Check if the check digit is valid
        if check_digit != int(isbn[12]):
            return False

    # If the input is not a valid ISBN-10 or ISBN-13, return False
    else:
        return False

    # If the input is a valid ISBN, return True
    return True
