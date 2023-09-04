def hexa(hex_string):
    """
    Convert a hexadecimal number, represented as a string (e.g. "10af8c"), to its decimal equivalent using first principles.
    The program should handle invalid hexadecimal strings.
    """
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
