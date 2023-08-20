def spiral_matrix(size):
    # Initialize an empty matrix
    matrix = [[0]*size for _ in range(size)]
    
    # Initialize the current number and position
    num = 1
    pos = (0, 0)
    
    # While the current number is less than or equal to the square of the size
    while num <= size*size:
        # Fill the current row from left to right
        for i in range(pos[1], size-pos[1]):
            matrix[pos[0]][i] = num
            num += 1
        
        # Fill the current column from top to bottom
        for i in range(pos[0]+1, size-pos[0]):
            matrix[i][size-pos[1]-1] = num
            num += 1
        
        # Fill the next row from right to left
        for i in range(size-pos[1]-2, pos[1]-1, -1):
            matrix[size-pos[0]-1][i] = num
            num += 1
        
        # Fill the next column from bottom to top
        for i in range(size-pos[0]-2, pos[0]+1, -1):
            matrix[i][pos[1]] = num
            num += 1
        
        # Increment the current position
        pos = (pos[0]+1, pos[1]+1)
    
    return matrix
