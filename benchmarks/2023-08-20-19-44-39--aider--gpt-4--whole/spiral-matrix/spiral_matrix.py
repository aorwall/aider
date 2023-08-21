def spiral_matrix(size):
    # Initialize the matrix with zeros
    matrix = [[0]*size for _ in range(size)]
    
    # Initialize the directions of movement
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize the current direction, row, and column
    direction = 0
    row = 0
    col = 0
    
    for i in range(1, size*size + 1):
        # Fill the current cell
        matrix[row][col] = i
        
        # Calculate the next row and column
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        
        # If the next cell is within the matrix and has not been filled yet, move to it
        if 0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] == 0:
            row = next_row
            col = next_col
        else:
            # Otherwise, change direction and move to the next cell in the new direction
            direction = (direction + 1) % 4
            row += directions[direction][0]
            col += directions[direction][1]
    
    return matrix
