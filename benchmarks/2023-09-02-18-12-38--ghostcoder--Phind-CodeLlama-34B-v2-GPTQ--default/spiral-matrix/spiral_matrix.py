def spiral_matrix(size):
    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    # Variables to keep track of the current position and direction
    pos = [0, 0]
    dirc = [0, 1]

    # Variable to keep track of the next number in sequence
    num = 1

    # Loop until all cells in the matrix have been filled
    while num <= size * size:
        # Fill the current cell
        matrix[pos[0]][pos[1]] = num

        # Update the position and calculate the next position
        new_pos = [pos[0] + dirc[0], pos[1] + dirc[1]]

        # Check if the new position is within the boundaries of the matrix
        # If it isn't, then we need to change our direction
        if (new_pos[0] < 0 or new_pos[0] >= size or new_pos[1] < 0 or new_pos[1] >= size or matrix[new_pos[0]][new_pos[1]] != 0):
            # Turn right and take a step forward
            if dirc == [0, 1]:
                dirc = [1, 0]
            elif dirc == [1, 0]:
                dirc = [0, -1]
            elif dirc == [0, -1]:
                dirc = [-1, 0]
            else:
                dirc = [0, 1]

            pos[0] += dirc[0]
            pos[1] += dirc[1]
        else:
            # Move to the new position
            pos = new_pos

        # Increment the number
        num += 1

    return matrix
