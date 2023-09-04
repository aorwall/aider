def annotate(minefield):
    """
    Returns a list of strings representing a completed Minesweeper board.
    
    Args:
        minefield: A list of strings representing the board.
        
    Returns:
        A list of strings representing the completed Minesweeper board.
    """
    rows = len(minefield)
    cols = len(minefield[0])
    new_minefield = []
    for row in range(rows):
        new_row = ""
        for col in range(cols):
            if minefield[row][col] != "*":
                count = 0
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if 0 <= row + r < rows and 0 <= col + c < cols:
                            count += int(minefield[row+r][col+c] == "*")
                new_row += str(count)
            else:
                new_row += "*"
        new_minefield.append(new_row)
    return new_minefield
