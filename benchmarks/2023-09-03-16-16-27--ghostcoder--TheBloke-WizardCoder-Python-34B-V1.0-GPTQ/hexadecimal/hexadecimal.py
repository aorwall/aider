def hexa(hex_string):
    # Check if input is valid hexadecimal string
    try:
        int(hex_string, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")


    # Convert hexadecimal string to decimal
    decimal = 0
    for index, char in enumerate(reversed(hex_string)):
        if char.isdigit():
            decimal += int(char) * (16 ** index)
        elif char.upper() >= 'A':
            decimal += (ord(char.upper()) - ord('A') + 10) * (16 ** index)
        else:
            decimal += (ord(char.lower()) - ord('a') + 10) * (16 ** index)

    return decimal
