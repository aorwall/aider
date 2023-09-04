def parse_binary(binary_string):
    try:
        return int(binary_string, 2)
    except ValueError:
        raise ValueError("Invalid binary literal: " + binary_string)
