def hexa(hex_string):
    decimal = 0
    hex_string = hex_string[::-1].lower()
    for i, char in enumerate(hex_string):
        if '0' <= char <= '9':
            decimal += int(char) * (16 ** i)
        elif 'a' <= char <= 'f':
            decimal += (ord(char) - ord('a') + 10) * (16 ** i)
        else:
            raise ValueError("Invalid hexadecimal digit: {}".format(char))
    return decimal
