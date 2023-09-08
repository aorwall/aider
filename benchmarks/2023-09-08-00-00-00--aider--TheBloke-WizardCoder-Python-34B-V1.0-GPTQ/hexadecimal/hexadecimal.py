def hexa(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    
    hex_string = hex_string.lower()
    hex_digits = "0123456789abcdef"
    
    decimal = 0
    for i, digit in enumerate(reversed(hex_string)):
        if digit not in hex_digits:
            raise ValueError("Invalid hexadecimal string")
        decimal += hex_digits.index(digit) * (16 ** i)
    
    return decimal
