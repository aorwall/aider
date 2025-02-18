def rows(row_count):
    """Return Pascal's triangle up to the nth row."""
    if row_count < 0:
        raise ValueError("Number of rows must be zero or positive.")
    elif row_count == 0:
        return []
    else:
        result = [[1]]
        for i in range(1, row_count):
            last_row = result[-1]
            next_row = [1] + [last_row[j] + last_row[j+1] for j in range(len(last_row)-1)] + [1]
            result.append(next_row)
        return result
