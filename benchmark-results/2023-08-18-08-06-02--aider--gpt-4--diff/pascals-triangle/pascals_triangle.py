def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    # Recursive case
    previous_rows = rows(row_count - 1)
    last_row = previous_rows[-1]
    current_row = [1] + [last_row[i-1] + last_row[i] for i in range(1, len(last_row))] + [1]
    return previous_rows + [current_row]
