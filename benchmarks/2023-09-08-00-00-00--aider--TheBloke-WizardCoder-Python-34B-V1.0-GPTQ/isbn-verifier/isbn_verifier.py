def is_valid(isbn):
    """
    Check if the provided string is a valid ISBN-10.

    :param isbn: string, the ISBN to check
    :return: bool, True if the ISBN is valid, False otherwise
    """
    # Remove dashes and convert to list of digits
    digits = [int(d) if d.isdigit() else 10 for d in isbn.replace('-', '').strip()]

    # Calculate the check digit
    check_digit = sum(d * (10 - i) for i, d in enumerate(digits[:-1])) % 11

    # Compare the check digit with the last digit
    return check_digit == digits[-1]
