import math

def saddle_points(matrix):
    num_rows = len(matrix) 
    num_cols = len(matrix[0])

    if not all(len(row) == num_cols for row in matrix):
        raise ValueError("irregular matrix")

    saddle_points = []

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] <= max(matrix[row]) and matrix[row][col] >= min(col_values(matrix, col)):
                saddle_points.append((row, col))

    return list(saddle_points)

def col_values(matrix, col_index):
    return [row[col_index] for row in matrix]
