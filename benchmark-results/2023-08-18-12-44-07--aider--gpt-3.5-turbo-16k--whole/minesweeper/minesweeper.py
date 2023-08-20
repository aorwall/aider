def annotate(minefield):
    # Check if minefield is empty
    if not minefield:
        return minefield

    # Get the dimensions of the minefield
    rows = len(minefield)
    cols = len(minefield[0])

    # Create a new minefield to store the counts
    counts = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Iterate over each cell in the minefield
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is a mine
            if minefield[i][j] == '*':
                counts[i][j] = '*'
            else:
                # Count the number of adjacent mines
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # Skip the current cell
                        if dx == 0 and dy == 0:
                            continue
                        # Calculate the coordinates of the adjacent cell
                        x = i + dx
                        y = j + dy
                        # Check if the adjacent cell is within the minefield
                        if 0 <= x < rows and 0 <= y < cols:
                            # Check if the adjacent cell is a mine
                            if minefield[x][y] == '*':
                                count += 1
                # Update the count in the counts minefield
                if count > 0:
                    counts[i][j] = str(count)

    return counts
