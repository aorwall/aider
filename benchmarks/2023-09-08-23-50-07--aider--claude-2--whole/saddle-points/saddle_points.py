def saddle_points(matrix):
  if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    raise ValueError("matrix must be a list of lists")
  
  if not all(len(row) == len(matrix[0]) for row in matrix):
    raise ValueError("irregular matrix")

  saddle_points = []

  num_rows = len(matrix)
  num_cols = len(matrix[0])

  for row_idx in range(num_rows):
    row = matrix[row_idx]
    max_in_row = max(row)

    for col_idx in range(num_cols):
      if row[col_idx] == max_in_row:
        min_in_col = min(matrix[i][col_idx] for i in range(num_rows))
        if row[col_idx] == min_in_col:
          saddle_points.append([row_idx, col_idx])

  return saddle_points
