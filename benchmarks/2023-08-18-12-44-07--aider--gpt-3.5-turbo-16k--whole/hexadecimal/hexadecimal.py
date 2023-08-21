def hexa(hex_string):
    decimal = 0
    power = 0

    for i in range(len(hex_string) - 1, -1, -1):
        char = hex_string[i]
        if char.isdigit():
            decimal += int(char) * (16 ** power)
        elif char.isalpha() and char.lower() in 'abcdef':
            decimal += (ord(char.lower()) - ord('a') + 10) * (16 ** power)
        else:
            raise ValueError("Invalid hexadecimal string")

        power += 1

    return decimal
