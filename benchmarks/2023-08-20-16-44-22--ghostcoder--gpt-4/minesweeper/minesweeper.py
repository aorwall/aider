def annotate(minefield):
    # Check if minefield is empty
    if not minefield:
        return []

    # Get the dimensions of the minefield
    rows, cols = len(minefield), len(minefield[0])

    # Check if minefield is malformed
    for row in minefield:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")

    # Initialize the result with the same dimensions as the minefield
    result = [[' ']*cols for _ in range(rows)]

    # Iterate over each cell in the minefield
    for i in range(rows):
        for j in range(cols):
            # If the cell is a mine, copy it to the result
            if minefield[i][j] == '*':
                result[i][j] = '*'
                continue

            # Count the number of mines in the 8 cells surrounding the current cell
            count = 0
            for x in range(max(0, i-1), min(rows, i+2)):
                for y in range(max(0, j-1), min(cols, j+2)):
                    if minefield[x][y] == '*':
                        count += 1

            # Replace the cell with the count if it's not 0
            if count != 0:
                result[i][j] = str(count)

    # Convert each row in the result to a string
    result = [''.join(row) for row in result]

    return result