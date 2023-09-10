def annotate(minefield):
  """
  Add the mine counts to a completed Minesweeper board.

  Minesweeper is a popular game where the user has to find the mines using numeric hints that indicate how many mines are directly adjacent (horizontally, vertically, diagonally) to a square.

  In this exercise you have to create some code that counts the number of mines adjacent to a given empty square and replaces that square with the count.

  The board is a rectangle composed of blank space (' ') characters.
  A mine is represented by an asterisk (`*`) character.

  If a given space has no adjacent mines at all, leave that square blank.

  Args:
    minefield: A string representing the Minesweeper board.

  Returns:
    A string representing the annotated Minesweeper board.
  """

  # Check if the input is valid.
  if not minefield:
    raise ValueError("The board is empty.")

  # Initialize the output board.
  annotated_board = minefield[:]

  # Iterate over the board and count the number of mines adjacent to each empty square.
  for row in range(len(minefield)):
    for column in range(len(minefield[row])):
      if minefield[row][column] == ' ':
        # Count the number of mines adjacent to the current square.
        mine_count = 0
        for row_offset in range(-1, 2):
          for column_offset in range(-1, 2):
            if row + row_offset < 0 or row + row_offset >= len(minefield):
              continue
            if column + column_offset < 0 or column + column_offset >= len(minefield[row]):
              continue
            if minefield[row + row_offset][column + column_offset] == '*':
              mine_count += 1

        # Replace the empty square with the mine count.
        annotated_board[row][column] = str(mine_count)

  # Return the annotated board.
  return annotated_board
