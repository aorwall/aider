def annotate(minefield):
    """
    Returns a completed minesweeper board.
    
    Args:
        minefield (list[list[str]]): The minefield, represented as a 2D list of str.
    
    Returns:
        list[list[str]]: The completed minesweeper board, represented as a 2D list of str.
    """
    # Create a copy of the minefield to avoid modifying the original
    minefield_copy = [row[:] for row in minefield]

    # Loop through the minefield
    for y, row in enumerate(minefield_copy):
        for x, cell in enumerate(row):
            # If the cell is a mine, skip it
            if cell == "*":
                continue

            # Count the number of mines in the surrounding cells
            mine_count = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    # Check that the cell is within the minefield's boundaries
                    if 0 <= y + dy < len(minefield_copy) and 0 <= x + dx < len(row):
                        # If the cell is a mine, increment the mine count
                        if minefield_copy[y + dy][x + dx] == "*":
                            mine_count += 1

            # If the mine count is non-zero, replace the cell with the mine count
            if mine_count != 0:
                minefield_copy[y][x] = str(mine_count)

    return minefield_copy
