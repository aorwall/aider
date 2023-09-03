def rectangles(strings):
    def is_corner(i, j):
        return i > 0 and strings[i-1][j] == '-' or j > 0 and strings[i][j-1] == '+'

    def count_rectangles(i, j):
        if not inside_rectangle:
            return 0

        # Check for the upper left corner of a rectangle
        if is_corner(i, j):
            width = 1
            while j + width < len(strings[i]) and strings[i][j+width] == '+':
                height = 1
                while i + height < len(strings) and strings[i+height][j] == '|':
                    if strings[i+height][j+width] == '+':
                        height += 1
                    else:
                        break
                if height >= 2 and width >= 2:
                    return (height - 1) * (width - 1)
                else:
                    return 0
        return 0
    rect_count = 0
    inside_rectangle = False
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == '+':
                if is_corner(i, j):
                    rect_count += count_rectangles(i, j)
                    inside_rectangle = True
            elif strings[i][j] != '+' and inside_rectangle:
                inside_rectangle = False
    return rect_count
