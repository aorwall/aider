def count_rectangles(diagram):
    rows = diagram.splitlines()
    cols = len(rows)
    total_rectangles = 0
    for row in rows:
        for col in range(cols - 1):
            if row[col] == '+' and row[col + 1] == '+':
                total_rectangles += 1
    return total_rectangles