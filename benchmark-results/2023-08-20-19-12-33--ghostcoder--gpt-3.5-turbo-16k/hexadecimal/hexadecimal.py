def hexa(hex_string):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    decimal = 0
    power = len(hex_string) - 1

    for digit in hex_string:
        if digit.lower() not in hex_dict:
            return None
        decimal += hex_dict[digit.lower()] * (16 ** power)
        power -= 1

    return decimal