def rows(row_count):
    # Check if row_count is less than 0
    if row_count < 0:
        raise ValueError("Number of rows cannot be negative.")

    def compute_row(n):
        """Compute nth row of Pascal's Triangle."""
        row = [1]
        for k in range(1, n):
            row.append((row[-1] * (n - k)) // k)
        return row

    triangle = []
    for i in range(row_count):
        triangle.append(compute_row(i + 1))

    return triangle
