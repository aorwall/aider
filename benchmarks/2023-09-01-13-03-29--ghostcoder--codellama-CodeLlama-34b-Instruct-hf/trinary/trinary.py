def trinary(string):
    # Check if the input string is a valid trinary number
    if not is_valid_trinary(string):
        return 0

    # Initialize the decimal equivalent to 0
    decimal = 0

    # Iterate through each character in the input string
    for i, char in enumerate(string):
        # Get the integer value of the current character
        char_value = int(char)

        # Calculate the decimal equivalent of the current character
        # by multiplying its value with the base 3 value of the current place
        decimal += char_value * 3 ** (len(string) - i - 1)

    return decimal

def is_valid_trinary(string):
    # Check if all characters in the input string are valid trinary digits (0, 1, or 2)
    return all(char in "012" for char in string)