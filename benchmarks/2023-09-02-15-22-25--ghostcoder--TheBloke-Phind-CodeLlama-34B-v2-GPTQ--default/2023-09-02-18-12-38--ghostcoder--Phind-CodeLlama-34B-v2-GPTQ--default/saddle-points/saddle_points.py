def saddle_points(matrix):
    # Check for irregular matrix
    if len(set(map(len, matrix))) > 1:
        raise ValueError("Irregular matrix")

    points = []

    # Iterate over rows
    for i in range(len(matrix)):
        max_row = max(matrix[i])

        # Iterate over columns
        for j in range(len(matrix[i])):
            min_column = min(col[j] for col in matrix)

            if matrix[i][j] == max_row and matrix[i][j] < min_column:
                points.append({'row': i, 'column': j})

    return points
