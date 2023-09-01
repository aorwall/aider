def annotate(minefield):
    """
    Add the mine counts to a completed Minesweeper board.
    
    Args:
        minefield (list[list[str]]): The Minesweeper board.
    
    Returns:
        list[list[str]]: The updated Minesweeper board with mine counts.
    """
    # Initialize the updated board with the same dimensions as the original board
    updated_board = [[0 for _ in range(len(minefield[0]))] for _ in range(len(minefield))]

    # Loop through each row and column of the board
    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            # Check if the current cell is a mine
            if minefield[i][j] == '*':
                # Increment the mine count for the surrounding cells
                for k in range(max(0, i - 1), min(len(minefield) - 1, i + 1)):
                    for l in range(max(0, j - 1), min(len(minefield[i]) - 1, j + 1)):
                        updated_board[k][l] += 1

    return updated_board
