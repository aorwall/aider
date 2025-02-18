def saddle_points(matrix):
    """
    Returns a list of tuples containing the coordinates of each saddle point
    in the given matrix.
    """
    # Check if the input is valid
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Invalid input")

    # Initialize variables
    m = len(matrix)
    n = len(matrix[0])
    result = []

    # Iterate over each element in the matrix
    for i in range(m):
        for j in range(n):
            # Check if the current element is a saddle point
            if _is_saddle_point(i, j, matrix):
                result.append((i, j))

    return result

def _is_saddle_point(i, j, matrix):
    """
    Returns True if the element at position (i, j) is a saddle point, False otherwise.
    """
    # Get the row and column of the current element
    row = matrix[i]
    col = [matrix[k][j] for k in range(len(matrix))]

    # Check if the current element is greater than or equal to
    # all elements in its row and less than or equal to all elements
    # in its column
    return row[j] >= max(row) and col[i] <= min(col)
