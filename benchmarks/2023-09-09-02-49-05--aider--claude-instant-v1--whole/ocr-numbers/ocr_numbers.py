def convert(input_grid):

    if not isinstance(input_grid, list):
        raise TypeError("Input must be a list of strings")

    rows = len(input_grid)
    cols = max(len(row) for row in input_grid)

    if rows % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if cols % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    # TODO: implement number recognition
    return '?'
