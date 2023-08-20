def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)

    decimal = 0
    for i, bit in enumerate(binary_string[::-1]):
        decimal += int(bit) * (2 ** i)
    return decimal