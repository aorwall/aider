def hexa(hex_string):
    # Define a dictionary for all possible hexadecimal digits
    hex_dict = {str(i): i for i in range(10)}
    hex_dict.update({"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15})

    # Check if the input is valid
    for char in hex_string:
        if char.upper() not in hex_dict:
            raise ValueError("Invalid hexadecimal string")

    # Convert the hexadecimal number to its decimal equivalent
    decimal = 0
    power = len(hex_string) - 1
    for char in hex_string:
        decimal += hex_dict[char.upper()] * (16 ** power)
        power -= 1

    return decimal
