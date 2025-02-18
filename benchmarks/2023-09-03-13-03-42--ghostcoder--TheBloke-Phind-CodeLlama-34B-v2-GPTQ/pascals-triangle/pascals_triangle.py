def rows(row_count):
    """Generate rows of Pascal's Triangle up to row_count."""
    if row_count < 0:
        raise ValueError("Number of rows cannot be negative.")

    result = [[1]]

    def compute_next_row(previous_row):
        next_row = []
        for index in range(len(previous_row)):
            next_value = (index == len(previous_row) - 1) \
                         and 1 \
                         or sum([previous_row[index], previous_row[index + 1]])
            next_row.append(next_value)
        return next_row

    while len(result) < row_count:
        result.append(compute_next_row(result[-1]))

    return result[:row_count]
