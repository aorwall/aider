def saddle_points(matrix):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Check if the matrix is irregular
    num_columns = len(matrix[0])
    if any(len(row) != num_columns for row in matrix):
        raise ValueError("irregular matrix")

    # Find the saddle points
    saddle_points = []
    num_rows = len(matrix)
    for i in range(num_rows):
        row = matrix[i]
        max_in_row = max(row)
        for j in range(num_columns):
            if row[j] == max_in_row:
                column = [matrix[k][j] for k in range(num_rows)]
                min_in_column = min(column)
                if row[j] == min_in_column:
                    saddle_points.append({"row": i, "column": j})

    return saddle_points
