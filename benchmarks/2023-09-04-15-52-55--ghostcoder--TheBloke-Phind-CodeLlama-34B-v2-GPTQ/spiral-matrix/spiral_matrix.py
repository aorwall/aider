def spiral_matrix(size):
    matrix = [[0]*size for _ in range(size)]
    number = 1
    left = 0
    top = 0
    right = size - 1
    bottom = size - 1

    while True:
        # Move right
        for i in range(left, right+1):
            matrix[top][i] = number
            number += 1
        top += 1
        if top > bottom or left > right: break

        # Move down
        for i in range(top, bottom+1):
            matrix[i][right] = number
            number += 1
        right -= 1
        if top > bottom or left > right: break

        # Move left
        for i in range(right, left-1, -1):
            matrix[bottom][i] = number
            number += 1
        bottom -= 1
        if top > bottom or left > right: break

        # Move up
        for i in range(bottom, top-1, -1):
            matrix[i][left] = number
            number += 1
        left += 1
        if top > bottom or left > right: break

    return matrix
