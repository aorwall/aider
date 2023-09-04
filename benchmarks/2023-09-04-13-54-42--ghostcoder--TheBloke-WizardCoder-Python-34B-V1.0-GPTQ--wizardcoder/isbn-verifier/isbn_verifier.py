import re

def is_valid(isbn):
    # Remove all non-digit characters except 'X' and convert to uppercase
    cleaned_isbn = re.sub('[^0-9X]', '', isbn).upper()

    if len(cleaned_isbn) != 10 or 'X' not in cleaned_isbn:
        return False

    try:
        total = sum((i + 1) * int(x) for i, x in enumerate(cleaned_isbn))
    except ValueError:
        return False

    checksum = 11 - (total % 11)

    if checksum == 10:
        check_char = 'X'
    elif checksum == 11:
        check_char = '0'
    else:
        check_char = str(checksum)

    return cleaned_isbn[-1] == check_char
