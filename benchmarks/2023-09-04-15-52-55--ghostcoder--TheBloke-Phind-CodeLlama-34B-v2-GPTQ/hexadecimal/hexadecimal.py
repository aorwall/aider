def hexa(hex_string):
    valid_chars = set('0123456789abcdefABCDEF')

    # Check if input is valid hexadecimal
    if any((char not in valid_chars) for char in hex_string):
        raise ValueError("Invalid hexadecimal string")

    total = 0
    power = len(hex_string) - 1

    for digit in hex_string:
        x = int(digit, 16) * (16 ** power)
        total += x
        power -= 1

    return total
