def hexa(hex_string):
    """
    Convert a hexadecimal number, represented as a string (e.g. "10af8c"), to its decimal equivalent using first principles.
    """
    # Check if the input is a valid hexadecimal string
    if not is_valid_hex(hex_string):
        raise ValueError("Invalid hexadecimal string")

    # Convert the hexadecimal string to an integer
    hex_int = int(hex_string, 16)

    # Convert the integer to a binary string
    bin_string = bin(hex_int)

    # Convert the binary string to a decimal string
    dec_string = int(bin_string, 2)

    return dec_string

def is_valid_hex(hex_string):
    """
    Check if a string is a valid hexadecimal number.
    """
    # Check if the string is empty
    if not hex_string:
        return False

    # Check if the string contains only hexadecimal characters (0-9, a-f, A-F)
    if not all(c in "0123456789abcdefABCDEF" for c in hex_string):
        return False

    return True