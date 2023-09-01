def spiral_matrix(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    num = 1
    start_row = 0
    start_col = 0
    end_row = size - 1
    end_col = size - 1
    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            matrix[start_row][col] = num
            num += 1
        start_row += 1
        for row in range(start_row, end_row + 1):
            matrix[row][end_col] = num
            num += 1
        end_col -= 1
        if start_row <= end_row:
            for col in range(end_col, start_col - 1, -1):
                matrix[end_row][col] = num
                num += 1
            end_row -= 1
        if start_col <= end_col:
            for row in range(end_row, start_row - 1, -1):
                matrix[row][start_col] = num
                num += 1
            start_col += 1
    return matrix
