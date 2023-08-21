def annotate(minefield):
    # Check if minefield is empty
    if not minefield:
        return []

    # Check if all rows have the same length
    if len(set(len(row) for row in minefield)) > 1:
        raise ValueError("All rows must have the same length.")

    # Check if minefield contains only valid characters
    if any(char not in ' *' for row in minefield for char in row):
        raise ValueError("Minefield can only contain spaces and asterisks.")

    # Initialize the result with the same size as minefield
    result = [list(row) for row in minefield]

    # Define the directions for adjacent cells
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Iterate over each cell in the minefield
    for i in range(len(minefield)):
        for j in range(len(minefield[0])):
            # If the cell is not a mine
            if minefield[i][j] != '*':
                # Count the number of mines in the adjacent cells
                mines = sum(minefield[i + dx][j + dy] == '*' for dx, dy in directions if 0 <= i + dx < len(minefield) and 0 <= j + dy < len(minefield[0]))
                # Replace the cell with the count if there are any mines, otherwise leave it blank
                result[i][j] = str(mines) if mines else ' '

    # Return the result as a list of strings
    return [''.join(row) for row in result]
