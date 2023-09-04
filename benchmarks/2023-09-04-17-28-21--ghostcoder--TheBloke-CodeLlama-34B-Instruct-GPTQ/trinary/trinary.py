def trinary(string):
    """Converts a trinary number, represented as a string, to its decimal equivalent."""
    # Initialize variables
    decimal = 0
    power = len(string) - 1

    # Iterate over each character in the input string
    for char in string:
        if char not in ['0', '1', '2']:
            raise ValueError("Invalid trinary digit {}".format(char))

        # Convert the current character to an integer
        digit = int(char, 3)

        # Calculate the decimal value of the current digit
        decimal += digit * 3 ** power

        # Decrement the power for the next iteration
        power -= 1

    return decimal
