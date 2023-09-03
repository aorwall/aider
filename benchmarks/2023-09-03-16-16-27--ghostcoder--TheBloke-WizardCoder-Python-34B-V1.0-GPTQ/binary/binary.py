def parse_binary(binary_string):
    """Converts a binary string into its decimal representation.
    
    Args:
        binary_string (str): A string representing a binary number.
    
    Returns:
        int: The integer value of the binary string.
    
    Raises:
        ValueError: If the input is not a valid binary literal.
    
    Examples:
        >>> parse_binary('101')
        5
        >>> parse_binary('1101010')
        22
        >>> parse_binary('abc')
        ValueError: Invalid binary literal: abc
    """
    # Check if all characters in the string are either '0' or '1'.
    if not all(char in ('0', '1') for char in binary_string):
        raise ValueError("Invalid binary literal: {}".format(binary_string))

    return int(binary_string, 2)
