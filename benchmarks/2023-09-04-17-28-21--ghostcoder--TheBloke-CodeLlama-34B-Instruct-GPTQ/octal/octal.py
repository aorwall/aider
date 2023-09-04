def parse_octal(digits):
    """
    Converts an octal string to its decimal equivalent.
    
    Args:
        digits (str): An octal representation of an integer.
    
    Returns:
        int: The decimal equivalent of the input octal string.
    """
    value = 0
    for char in digits:
        value = (value << 3) | (int(char, 8) & 0x7)
    return value
