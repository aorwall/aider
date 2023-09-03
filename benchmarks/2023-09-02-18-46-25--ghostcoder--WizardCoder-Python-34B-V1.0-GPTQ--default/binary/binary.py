def parse_binary(binary_string):
    """Converts a binary string to its decimal equivalent using first principles"""

    # Check for invalid input
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)

    # Initialize variables
    decimal = 0
    length = len(binary_string) - 1

    # Iterate through each digit of the binary number
    for i, digit in enumerate(reversed(binary_string)):
        decimal += int(digit) * (2 ** i)

    return decimal
