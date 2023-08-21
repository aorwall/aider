def rectangles(strings):
    height = len(strings)
    width = len(strings[0]) if height else 0
    count = 0

    for i in range(height):
        for j in range(width):
            if strings[i][j] == '+':
                for k in range(j + 1, width):
                    if strings[i][k] == '+':
                        for l in range(i + 1, height):
                            if strings[l][j] == '+' and strings[l][k] == '+':
                                if all(strings[i][m] in '+-' for m in range(j, k)) and \
                                   all(strings[n][j] in '+|' for n in range(i, l)) and \
                                   all(strings[i][m] in '+-' for m in range(j, k)) and \
                                   all(strings[n][k] in '+|' for n in range(i, l)):
                                    count += 1
    return count