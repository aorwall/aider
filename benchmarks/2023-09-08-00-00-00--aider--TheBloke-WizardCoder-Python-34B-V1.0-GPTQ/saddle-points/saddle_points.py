def saddle_points(matrix):
    """
    Finds saddle points in a given matrix.

    A saddle point is a cell whose value is greater than or equal to the maximum value in its row and less than or equal to the minimum value in its column.

    Args:
        matrix (list of lists): The matrix to search for saddle points.

    Returns:
        list of tuples: The coordinates of the saddle points in the matrix.
    """

    if not matrix or not matrix[0]:
        raise ValueError("empty matrix")

    rows, cols = len(matrix), len(matrix[0])
    saddle_points = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == max(matrix[row]) and matrix[row][col] == min(row_col for row_col in zip(*matrix)):
                saddle_points.append((row, col))

    return saddle_points
