def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    elif row_count == 1:
        return [[1]]
    else:
        new_row = [1]
        last_row = rows(row_count - 1)[-1]
        new_row += [sum(pair) for pair in zip(last_row[:-1], last_row[1:])]
        new_row.append(1)
        return rows(row_count - 1) + [new_row]