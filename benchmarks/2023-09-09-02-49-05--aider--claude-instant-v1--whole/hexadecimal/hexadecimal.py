import re

def hexa(hex_string):
    if not re.match(r"^[0-9a-fA-F]+$", hex_string):
        raise ValueError("Invalid hexadecimal string")

    decimal = 0
    for char in hex_string:
        decimal = decimal * 16 + int(char, 16)

    return decimal
