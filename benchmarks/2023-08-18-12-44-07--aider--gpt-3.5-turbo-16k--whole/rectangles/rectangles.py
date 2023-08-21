def rectangles(strings):
    # Count the number of rectangles in the ASCII diagram
    count = 0

    # Find the coordinates of '+' characters
    plus_coords = []
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == '+':
                plus_coords.append((i, j))

    # Iterate through the '+' coordinates and check for rectangles
    for i in range(len(plus_coords)):
        for j in range(i + 1, len(plus_coords)):
            top_left = plus_coords[i]
            bottom_right = plus_coords[j]

            # Check if the top left and bottom right coordinates form a rectangle
            if is_rectangle(strings, top_left, bottom_right):
                count += 1

    return count


def is_rectangle(strings, top_left, bottom_right):
    # Check if the given coordinates form a rectangle
    x1, y1 = top_left
    x2, y2 = bottom_right

    # Check if the top and bottom lines are '-' characters
    for i in range(y1 + 1, y2):
        if strings[x1][i] != '-' or strings[x2][i] != '-':
            return False

    # Check if the left and right lines are '|' characters
    for i in range(x1 + 1, x2):
        if strings[i][y1] != '|' or strings[i][y2] != '|':
            return False

    return True
