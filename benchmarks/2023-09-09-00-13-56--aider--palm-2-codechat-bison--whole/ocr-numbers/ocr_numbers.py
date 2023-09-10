def convert(input_grid):
  """Converts a 3x4 grid of pipes, underscores, and spaces to a string containing 0-9, or '?' if the input is garbled.

  Args:
    input_grid: A string containing a 3x4 grid of pipes, underscores, and spaces.

  Returns:
    A string containing 0-9, or '?' if the input is garbled.
  """

  # Check that the input is the correct size.
  if len(input_grid) != 12:
    raise ValueError("Number of input lines is not a multiple of four")

  # Check that each line is the correct size.
  for line in input_grid.splitlines():
    if len(line) != 3:
      raise ValueError("Number of input columns is not a multiple of three")

  # Convert the input grid to a list of characters.
  input_grid = list(input_grid)

  # Check that each character is a pipe, an underscore, or a space.
  for character in input_grid:
    if character not in ["_", "|", " "]:
      raise ValueError("Input grid contains invalid character")

  # Convert the input grid to a string containing 0-9, or '?' if the input is garbled.
  output_grid = ""
  for i in range(3):
    for j in range(4):
      if input_grid[i * 4 + j] == "_":
        output_grid += "0"
      elif input_grid[i * 4 + j] == "|":
        output_grid += "1"
      else:
        output_grid += "?"

  return output_grid
