def saddle_points(matrix):
  """
  Finds all the potential trees where you could build your tree house.

  The data company provides the data as grids that show the heights of the trees.
  The rows of the grid represent the east-west direction, and the columns represent the north-south direction.

  An acceptable tree will be the largest in its row, while being the smallest in its column.

  A grid might not have any good trees at all.
  Or it might have one, or even several.

  Args:
    matrix: A 2D array of integers representing the heights of the trees.

  Returns:
    A list of tuples, where each tuple is the coordinates of a potential tree house.
  """

  # Check if the matrix is irregular.
  if not matrix:
    raise ValueError("empty matrix")
  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise ValueError("irregular matrix")

  # Find all the potential tree houses.
  potential_tree_houses = []
  for row_index, row in enumerate(matrix):
    for column_index, height in enumerate(row):
      if height == max(row) and height == min(matrix[column_index]):
        potential_tree_houses.append((row_index, column_index))

  return potential_tree_houses
