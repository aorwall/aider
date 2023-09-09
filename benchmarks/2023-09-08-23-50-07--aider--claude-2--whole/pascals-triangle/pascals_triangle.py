def rows(row_count):
  if row_count < 0:
    raise ValueError("number of rows is negative")

  if row_count == 0: 
    return []

  if row_count == 1:
    return [[1]]

  prev_row = rows(row_count-1)
  curr_row = [1]

  for i in range(1, row_count):
    curr_row.append(prev_row[i-1] + prev_row[i])

  curr_row.append(1)

  return prev_row + [curr_row]
