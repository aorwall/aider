def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    num = 1
    top, bottom = 0, size
    left, right = 0, size
    
    while num <= size**2:
        for i in range(left, right):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom):
            matrix[i][right-1] = num 
            num += 1
        right -= 1
        if top < bottom:
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = num
                num += 1
            bottom -= 1
        if left < right:
            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = num
                num += 1
        left += 1
    return matrix
