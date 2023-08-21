def annotate(minefield):
    if not all(len(row) == len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")
    
    valid_chars = {'*', ' '}
    if not all(cell in valid_chars for row in minefield for cell in row):
        raise ValueError("The board contains invalid characters.")
    
    completed_board = []
    for i, row in enumerate(minefield):
        completed_row = ''
        for j, cell in enumerate(row):
            if cell == '*':
                completed_row += '*'
            else:
                count = sum(minefield[i+di][j+dj] == '*' for di in range(-1, 2) for dj in range(-1, 2) if 0 <= i+di < len(minefield) and 0 <= j+dj < len(row))
                completed_row += str(count) if count > 0 else ' '
        completed_board.append(completed_row)
    
    return completed_board
