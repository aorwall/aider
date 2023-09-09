def parse_binary(binary_string):
    if not binary_string.isdecimal():
        raise ValueError("Invalid binary literal: " + binary_string + " contains non-binary digits")
        
    decimal = 0
    for char in binary_string:
        decimal = decimal * 2 + int(char)
        
    return decimal
