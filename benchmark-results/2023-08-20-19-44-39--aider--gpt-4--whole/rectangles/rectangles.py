def rectangles(strings):
    if not strings:
        return 0

    height = len(strings)
    width = len(strings[0])
    count = 0

    for i in range(height):
        for j in range(width):
            if strings[i][j] == '+':
                for k in range(i + 1, height):
                    if strings[k][j] == '+':
                        for l in range(j + 1, width):
                            if strings[i][l] == '+' and strings[k][l] == '+':
                                if all(strings[m][j] == '|' for m in range(i+1, k)) and \
                                   all(strings[m][l] == '|' for m in range(i+1, k)) and \
                                   all(strings[i][n] == '-' for n in range(j+1, l)) and \
                                   all(strings[k][n] == '-' for n in range(j+1, l)):
                                    count += 1
    return count
