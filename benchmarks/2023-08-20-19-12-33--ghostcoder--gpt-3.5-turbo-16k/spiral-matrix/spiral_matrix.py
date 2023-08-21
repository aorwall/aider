def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    num = 1
    row_start = 0
    row_end = size - 1
    col_start = 0
    col_end = size - 1

    while row_start <= row_end and col_start <= col_end:
        # Traverse right
        for i in range(col_start, col_end + 1):
            matrix[row_start][i] = num
            num += 1
        row_start += 1

        # Traverse down
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1

        # Traverse left
        for i in range(col_end, col_start - 1, -1):
            matrix[row_end][i] = num
            num += 1
        row_end -= 1

        # Traverse up
        for i in range(row_end, row_start - 1, -1):
            matrix[i][col_start] = num
            num += 1
        col_start += 1

    return matrix