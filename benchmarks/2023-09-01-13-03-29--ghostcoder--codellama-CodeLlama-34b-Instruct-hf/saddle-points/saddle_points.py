def saddle_points(matrix):
    """
    Returns a list of tuples containing the coordinates of each saddle point
    in the given matrix.
    """
    # Check if matrix is irregular
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Irregular matrix")

    # Initialize empty list to store saddle point coordinates
    saddle_points = []

    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Find the largest element in the row
        max_row_value = max(matrix[i])
        # Find the index of the largest element in the row
        max_row_index = matrix[i].index(max_row_value)

        # Check if the largest element in the row is the smallest element in the column
        if matrix[i][max_row_index] == min(matrix[max_row_index]):
            # If it is, add the coordinates to the list of saddle points
            saddle_points.append((i, max_row_index))

    return saddle_points
