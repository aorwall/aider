def saddle_points(matrix):
    """
    Returns a list of tuples containing the coordinates of the saddle points in a matrix.
    """
    if not is_matrix_regular(matrix):
        raise ValueError("Irregular matrix")

    saddle_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if is_saddle_point(matrix, i, j):
                saddle_points.append((i, j))

    return saddle_points

def is_matrix_regular(matrix):
    """
    Returns True if the matrix is regular, False otherwise.
    """
    # Check if the matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        return False

    # Check if the matrix is rectangular
    if not all(len(row) == len(matrix[0]) for row in matrix):
        return False

    return True

def is_saddle_point(matrix, i, j):
    """
    Returns True if the point at (i, j) is a saddle point, False otherwise.
    """
    # Check if the point is the largest in its row and the smallest in its column
    if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(matrix[j] for row in matrix):
        return True
    else:
        return False
