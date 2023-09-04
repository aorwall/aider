def spiral_matrix(size):
    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Set the boundaries of the matrix
    start_row = 0
    end_row = size - 1
    start_col = 0
    end_col = size - 1

    # Initialize the counter for the values
    count = 1

    while start_row <= end_row and start_col <= end_col:
        # Print the first row from the remaining rows
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = count
            count += 1
        start_row += 1

        # Print the last column from the remaining columns
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = count
            count += 1
        end_col -= 1

        # Print the last row from the remaining rows
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = count
                count += 1
            end_row -= 1

        # Print the first column from the remaining columns
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                matrix[i][start_col] = count
                count += 1
            start_col += 1

    return matrix
