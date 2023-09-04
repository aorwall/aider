def saddle_points(matrix):
    # Check if matrix is empty
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix must not be empty.")

    # Check if matrix is regular
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("Irregular matrix.")

    # Find saddle points
    saddle_point_sums = []
    for i in range(num_rows):
        max_in_col = max(matrix[i])
        for j in range(num_cols):
            min_in_row = min([row[j] for row in matrix])
            if max_in_col == min_in_row:
                saddle_point_sums.append({"row": i+1, "column": j+1})

    return saddle_point_sums
