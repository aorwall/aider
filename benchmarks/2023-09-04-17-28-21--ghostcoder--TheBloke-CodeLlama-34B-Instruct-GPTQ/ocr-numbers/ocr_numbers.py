def convert(input_grid):
    """
    Converts a grid of text representing numbers into a list of integers.
    
    Args:
        input_grid: A list of strings representing the input grid.
    
    Returns:
        A list of ints representing the numbers found in the grid.
    """
    numbers = []
    for row in range(len(input_grid)):
        for col in range(len(input_grid[row])):
            char = input_grid[row][col]
            if char == " ":
                continue
            elif char == "_":
                numbers.append(0)
            elif char == "|":
                numbers.append(1)
            else:
                raise ValueError("Invalid character encountered.")
    return numbers

