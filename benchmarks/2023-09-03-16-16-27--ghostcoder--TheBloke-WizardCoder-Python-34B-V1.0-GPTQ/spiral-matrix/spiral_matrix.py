def spiral_matrix(size):
    # Initialize empty matrix with zeros
    matrix = [[0] * size for _ in range(size)]

    # Define initial positions and directions
    top, bottom, left, right = 0, size - 1, 0, size - 1
    row, col = 0, 0
    direction = 'r'
    num = 1

    while True:
        # Fill top row
        if direction == 'r':
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1
        # Fill right column
        elif direction == 'd':
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
        # Fill bottom row
        elif direction == 'l':
            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
        # Fill left column
        else:
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        # Change direction after every iteration
        direction = {'r':'d', 'd':'l', 'l':'b', 'b':'r'}[direction]

        # Check if we finished iterating through the whole matrix
        if top > bottom or left > right:
            break

    return matrix
