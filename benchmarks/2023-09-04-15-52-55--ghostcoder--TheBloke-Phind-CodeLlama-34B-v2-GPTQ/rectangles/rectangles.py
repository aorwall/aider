def rectangles(diagram):
    count = 0
    # The input is a list of strings so we don't need to use strip() or split()
    lines = diagram
    height = len(lines)
    width = len(lines[0])

    for y in range(height - 1):
        for x in range(width - 1):
            if (lines[y][x] == "+" and lines[y][x + 1] == "+" and
                    lines[y + 1][x] == "+" and lines[y + 1][x + 1] == "+"):
                count += 1

    return count