def annotate(board):
    if not isinstance(board, list) or not all(isinstance(row, list) for row in board):
        raise ValueError("The board is invalid with current input.")

    def count_mines(x, y):
        count = 0
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == '*':
                count += 1
        return count

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                board[i][j] = str(count_mines(i, j))

    return board

# Test cases
print(annotate([[' ', '*', ' ', ' '], [' ', ' ', '*', ' '], [' ', '*', ' ', ' '], [' ', ' ', ' ', ' ']]))
print(annotate([['*', ' ', ' ', ' '], [' ', '*', ' ', ' '], [' ', '*', ' ', ' '], [' ', ' ', ' ', '*']]))
