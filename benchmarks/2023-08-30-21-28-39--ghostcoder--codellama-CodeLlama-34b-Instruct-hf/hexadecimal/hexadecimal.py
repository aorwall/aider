def hexa(hex_string):
    """
    Convert a hexadecimal number, represented as a string (e.g. "10af8c"), to its decimal equivalent using first principles.
    """
    # Initialize the result to 0
    result = 0

    # Iterate through each character in the hexadecimal string
    for char in hex_string:
        # Convert the character to an integer using the built-in ord() function
        digit = ord(char)

        # Check if the digit is a valid hexadecimal digit
        if digit >= ord('0') and digit <= ord('9'):
            digit -= ord('0')
        elif digit >= ord('a') and digit <= ord('f'):
            digit -= ord('a') - 10
        elif digit >= ord('A') and digit <= ord('F'):
            digit -= ord('A') - 10
        else:
            # If the digit is not a valid hexadecimal digit, raise an error
            raise ValueError("Invalid hexadecimal digit: {}".format(char))

        # Add the digit to the result
        result = result * 16 + digit

    # Return the result
    return result
