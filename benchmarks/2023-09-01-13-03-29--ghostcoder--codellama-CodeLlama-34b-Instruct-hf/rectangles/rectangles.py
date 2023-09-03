def count_rectangles(diagram):
    rectangles = 0
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "+":
                rectangles += 1
    return rectangles