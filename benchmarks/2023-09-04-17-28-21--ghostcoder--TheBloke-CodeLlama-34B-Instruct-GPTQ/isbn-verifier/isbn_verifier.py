import re

def is_valid(isbn):
    # Remove non-numeric characters and convert to list
    isbn = re.sub('[^0-9X]', '', str(isbn)).upper()
    isbn = list(isbn)

    # Convert last char to numeric value
    if isbn[-1] == 'X':
        isbn[-1] = 10
    else:
        isbn[-1] = int(isbn[-1])

    # Calculate sum
    total = 0
    for i, num in enumerate(isbn[:-1], start=1):
        total += i * int(num)

    # Checksum calculation
    remainder = total % 11
    checksum = 11 - remainder if remainder != 0 else 0

    # Compare calculated checksum with inputted checksum
    return True if checksum == isbn[-1] else False
