def hexa(hex_string):
    if not hex_string.startswith('0x'):
        raise ValueError("Invalid hexadecimal string")
    hex_string = hex_string[2:]
    result = 0
    for i in range(len(hex_string)):
        digit = hex_string[i]
        if digit.isdigit():
            result += int(digit) * 16 ** (len(hex_string) - i - 1)
        elif digit.islower():
            result += ord(digit) - ord('a') + 10 * 16 ** (len(hex_string) - i - 1)
        elif digit.isupper():
            result += ord(digit) - ord('A') + 10 * 16 ** (len(hex_string) - i - 1)
    return result
