def count_rectangles(diagram):
    def is_rectangle(lines):
        if len(lines) < 2:
            return False
        width = len(lines[0])
        for line in lines:
            if len(line) != width:
                return False
            if "+" not in line:
                return False
        return True

    def count_rectangles_in_lines(lines, row, col, count):
        if row >= len(lines) or col >= len(lines[row]):
            return count

        if lines[row][col] == "+":
            if is_rectangle([line[col:col+2] for line in lines[row:]]):
                count += 1
                lines[row][col] = "."
                count = count_rectangles_in_lines(lines, row, col + 1, count)
                lines[row][col] = "+"
            else:
                count = count_rectangles_in_lines(lines, row, col + 1, count)
        else:
            count = count_rectangles_in_lines(lines, row, col + 1, count)

        return count_rectangles_in_lines(lines, row + 1, col, count)

    lines = diagram.split("\n")
    return count_rectangles_in_lines(lines, 0, 0, 0)

# Test cases
print(count_rectangles("""
   +--+
  ++  |
+-++--+
|  |  |
+--+--+
"""))  # Should print 6
