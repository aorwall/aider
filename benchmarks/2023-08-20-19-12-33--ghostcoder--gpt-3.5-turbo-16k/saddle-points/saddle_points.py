def saddle_points(matrix):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check if the matrix is irregular
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("irregular matrix")

    saddle_points = []

    for i in range(num_rows):
        for j in range(num_cols):
            value = matrix[i][j]
            if value == max(matrix[i]) and value == min(row[j] for row in matrix):
                saddle_points.append({"row": i, "column": j})

    return saddle_points