def parse_binary(binary_string):
    if not all(char in '01' for char in binary_string):
        raise ValueError("Invalid binary literal: " + binary_string)
    
    return sum(int(bit) * 2**i for i, bit in enumerate(binary_string[::-1]))
