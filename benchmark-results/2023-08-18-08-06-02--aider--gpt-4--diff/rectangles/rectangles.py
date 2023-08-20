def rectangles(strings):
    # Parse the input into a 2D array of characters
    grid = [list(row) for row in strings]

    # Initialize the counter
    count = 0

    # Iterate over all pairs of points in the array
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(i + 1, len(grid)):
                for l in range(j + 1, len(grid[k])):
                    # Check if the current pair of points forms a rectangle
                    if grid[i][j] == '+' and grid[i][l] == '+' and grid[k][j] == '+' and grid[k][l] == '+':
                        # Check if all the sides of the rectangle are either '-' or '|'
                        if all(grid[i][m] in '+-' for m in range(j + 1, l)) and all(grid[k][m] in '+-' for m in range(j + 1, l)) and all(grid[n][j] in '+|' for n in range(i + 1, k)) and all(grid[n][l] in '+|' for n in range(i + 1, k)):
                            # If they do, increment the counter
                            count += 1

    # Return the counter
    return count
