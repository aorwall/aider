def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")

    saddle_points = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == max(row) and value == min(col[j] for col in matrix):
                saddle_points.append({"row": i, "column": j})

    return saddle_points
