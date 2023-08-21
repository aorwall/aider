def hexa(hex_string):
    hex_digits = set("0123456789abcdefABCDEF")
    if all(c in hex_digits for c in hex_string):
        return int(hex_string, 16)
    else:
        raise ValueError("Invalid hexadecimal string")
