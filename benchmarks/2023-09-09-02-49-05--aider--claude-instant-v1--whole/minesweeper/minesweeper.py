def annotate(minefield):

    if not validate_board(minefield):
        raise ValueError("The board is invalid with current input.")

    rows = len(minefield)
    cols = len(minefield[0])

    for row in range(rows):
        for col in range(cols):
            if minefield[row][col] == ' ':
                minefield[row][col] = count_mines(minefield, row, col)

    return minefield


def validate_board(board):
   # validation logic
   return True


def count_mines(board, row, col):
   count = 0
   for r in range(max(0, row-1), min(rows, row+2)):
      for c in range(max(0, col-1), min(cols, col+2)):
         if r != row or c != col:
            if board[r][c] == '*':
               count += 1
   return count
