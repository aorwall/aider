def annotate(minefield):
    if not minefield or not any('*' in row for row in minefield):
        return minefield

    rows = len(minefield)
    cols = len(minefield[0])

    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    res = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if minefield[r][c] != "*":
                count = sum((0 <= nr < rows and 0 <= nc < cols and minefield[nr][nc] == "*")
                           for dr, dc in directions
                           for nr, nc in [(r+dr, c+dc), (r-dr, c-dc)])
                row.append(str(count) if count > 0 else "*")
            else:
                row.append(minefield[r][c])
        res.append("".join(row))

    return "\n".join(res)
