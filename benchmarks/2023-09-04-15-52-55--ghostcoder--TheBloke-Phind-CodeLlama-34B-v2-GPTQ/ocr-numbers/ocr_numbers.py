def convert(input_grid):
    if len('\n'.join(input_grid)) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    # Add here the logic for converting the input_grid into output string
    pass

    return output_string

