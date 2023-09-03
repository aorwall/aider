def count_rectangles(diagram):
    rectangles = []
    lines = diagram.strip().split('\n')
    height = len(lines)
    width = len(lines[0])

    for y in range(height - 1):
        for x in range(width - 1):
            if lines[y][x] == '+' and lines[y][x+1] == '+' and lines[y+1][x] == '+' and lines[y+1][x+1] == '+':
                rectangles.append((x, y))

    return len(rectangles), rectangles

if __name__ == "__main__":
    import sys
    diagram = "\n".join([line.rstrip() for line in sys.stdin])
    print("Number of rectangles:", count_rectangles(diagram)[0])