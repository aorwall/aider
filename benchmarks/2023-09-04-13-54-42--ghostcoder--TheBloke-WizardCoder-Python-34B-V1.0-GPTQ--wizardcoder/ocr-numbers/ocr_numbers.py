def convert(input_grid):
    """
    Convert a 3x4 grid of pipes, underscores, and spaces into a string representing a number.
    
    Args:
        input_grid (list[str]): A list of strings representing the input grid. Each string represents a row in the grid, using pipes ('|'), underscores ('_'), and spaces (' ') for different values.
    
    Returns:
        str: A string representation of the number encoded by the input grid. If the input is invalid, returns '?'.
    
    Raises:
        ValueError: If the input has an invalid format (e.g., wrong number of rows or columns).
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Input must have a multiple of four lines.")

    if any(len(row) != 3 for row in input_grid):
        raise ValueError("All lines must have exactly three characters.")

    numbers = {
        (" _ ", "   ", "   "): "0",
        ("   ", "  |", "  |"): "1",
        (" _ ", "  |", " _|"): "2",
        (" _ ", "  |", " _|"): "3",
        ("   ", "|_|", "  |"): "4",
        (" _ ", "|_ ", " _|"): "5",
        (" _ ", "|_ ", "|_|"): "6",
        (" _ ", "  |", "  |"): "7",
        (" _ ", "|_|", "|_|"): "8",
        (" _ ", "|_|", " _|"): "9",
    }

    result = []
    for i in range(0, len(input_grid), 4):
        digit = tuple(input_grid[i+j][1:-1] for j in range(4))
        try:
            value = numbers[digit]
        except KeyError:
            return "?"

        result.append(value)

    return ','.join(result)

