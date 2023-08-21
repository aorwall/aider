def annotate(minefield):
    if not minefield:
        return minefield

    rows = len(minefield)
    cols = len(minefield[0])

    # Convert the minefield to a list of lists
    minefield = [list(row) for row in minefield]

    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == ' ':
                count = 0
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        if minefield[x][y] == '*':
                            count += 1
                if count > 0:
                    minefield[i][j] = str(count)

    # Convert the minefield back to a list of strings
    minefield = [''.join(row) for row in minefield]

    return minefield