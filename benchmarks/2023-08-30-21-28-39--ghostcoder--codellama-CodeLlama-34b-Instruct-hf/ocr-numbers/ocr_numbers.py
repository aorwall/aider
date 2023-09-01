def convert(input_grid):
    """
    Converts a 3x4 grid of pipes, underscores, and spaces into a string of binary digits.
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    binary_string = ""
    for row in input_grid:
        for column in row:
            if column == "|":
                binary_string += "1"
            elif column == "_":
                binary_string += "0"
            else:
                binary_string += "?"
    return binary_string

