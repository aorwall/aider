import re

def is_valid(isbn):
    # Remove all non-numeric characters and convert remaining characters to integers
    digits = [int(c) if c != "X" else 10 for c in re.sub(r'\D', '', isbn)]

    # Check that there are exactly 10 digits left after removing non-numeric characters
    if len(digits) != 10:
        return False

    # Calculate the sum of each digit multiplied by its position weight
    total = sum([digits[i] * (10 - i) for i in range(len(digits))])

    return total % 11 == 0
