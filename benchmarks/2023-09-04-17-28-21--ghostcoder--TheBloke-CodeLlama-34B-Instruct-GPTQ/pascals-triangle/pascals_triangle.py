def rows(row_count):
    """Return a list of lists representing Pascal's Triangle with the given number of rows."""
    result = []
    for i in range(row_count):
        row = [1] * (i + 1)
        if i > 0:
            for j in range(1, i):
                try:
                    row[j] = result[-1][j - 1] + result[-1][j]
                except IndexError:
                    raise ValueError("Negative rows are not allowed.")
        result.append(row)
    return result
