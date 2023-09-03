def annotate(minefield):
    if not minefield or any(len(row) != len(minefield[0]) for row in minefield):
        raise ValueError("Invalid board")
    rows = len(minefield)
    cols = len(minefield[0])

    res = [[0]*cols for _ in range(rows)]

    def count_mines(r, c):
        count = 0
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < rows and 0 <= nc < cols and minefield[nr][nc] == '*':
                count += 1

        return count

    for r in range(rows):
        for c in range(cols):
            if minefield[r][c] != '*':
                res[r][c] = str(count_mines(r, c)) if count_mines(r, c) > 0 else ' '
            else:
                res[r][c] = '*'

    return ["".join(row) for row in res]
