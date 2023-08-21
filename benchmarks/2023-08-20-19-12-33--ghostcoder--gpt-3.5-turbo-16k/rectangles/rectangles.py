def rectangles(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == '+':
                for k in range(i+1, len(strings)):
                    if strings[k][j] == '+':
                        for l in range(j+1, len(strings[i])):
                            if strings[i][l] == '+' and strings[k][l] == '+':
                                # Check if the other characters in the rectangle are valid
                                valid_rectangle = True
                                for m in range(i+1, k):
                                    if strings[m][j] != '|' or strings[m][l] != '|':
                                        valid_rectangle = False
                                        break
                                for n in range(j+1, l):
                                    if strings[i][n] != '-' or strings[k][n] != '-':
                                        valid_rectangle = False
                                        break
                                if valid_rectangle:
                                    count += 1
                            else:
                                break
                    else:
                        break
    return count