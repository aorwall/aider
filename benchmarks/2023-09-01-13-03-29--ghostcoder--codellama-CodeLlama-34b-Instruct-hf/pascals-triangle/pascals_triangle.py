def rows(row_count):
    """
    Returns a list of lists, where each list represents a row of Pascal's Triangle.
    """
    if row_count <= 0:
        raise ValueError("Number of rows must be positive")
    rows = []
    for i in range(row_count):
        rows.append(_compute_row(i))
    return rows

def _compute_row(row_index):
    """
    Returns a list of integers, where each integer represents the value at a position in a row of Pascal's Triangle.
    """
    row = []
    for j in range(row_index + 1):
        if j == 0 or j == row_index:
            row.append(1)
        else:
            row.append(row[j - 1] + row[j])
    return row
