def rows(row_count):
  """
  Computes Pascal's triangle up to a given number of rows.

  In Pascal's Triangle each number is computed by adding the numbers to the right and left of the current position in the previous row.

  Args:
    row_count: The number of rows to compute.

  Returns:
    A list of lists, where each inner list represents a row of Pascal's Triangle.

  Raises:
    ValueError: If the row_count is negative.
  """

  if row_count < 0:
    raise ValueError("row_count must be non-negative")

  # Initialize the first row.

  row = [1]

  # Iterate over the remaining rows.

  for i in range(1, row_count):
    # Compute the new row.

    new_row = [1]
    for j in range(1, i):
      new_row.append(row[j - 1] + row[j])
    new_row.append(1)

    # Update the row.

    row = new_row

  # Return the rows.

  return [row]
