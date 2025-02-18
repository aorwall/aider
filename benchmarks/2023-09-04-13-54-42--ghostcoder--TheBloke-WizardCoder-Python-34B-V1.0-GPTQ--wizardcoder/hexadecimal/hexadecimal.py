def hexa(hex_string):
    if not all(char in '0123456789abcdefABCDEF' for char in hex_string):
        raise ValueError('Invalid hexadecimal string')

    hex_dict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    decimal = 0
    length = len(hex_string)
    for i, digit in enumerate(reversed(hex_string)):
        decimal += hex_dict[digit] * (16 ** (length - 1 - i))

    return decimal
