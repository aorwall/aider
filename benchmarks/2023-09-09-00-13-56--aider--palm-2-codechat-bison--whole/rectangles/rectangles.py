def rectangles(strings):
  """
  Count the number of rectangles in an ASCII diagram.

  Args:
    strings: A list of strings that make up the ASCII diagram.

  Returns:
    The number of rectangles in the diagram.
  """

  # First, we need to find all of the rows in the diagram.
  rows = []
  for string in strings:
    if string:
      rows.append(string)

  # Now, we need to find all of the columns in the diagram.
  columns = []
  for i in range(len(rows[0])):
    for row in rows:
      if row[i] == '+':
        columns.append(i)

  # Now, we can count the number of rectangles.
  count = 0
  for i in range(len(rows) - 1):
    for j in range(len(columns) - 1):
      if rows[i][j] == '+' and rows[i + 1][j] == '+' and rows[i][j + 1] == '+' and rows[i + 1][j + 1] == '+':
        count += 1

  return count
