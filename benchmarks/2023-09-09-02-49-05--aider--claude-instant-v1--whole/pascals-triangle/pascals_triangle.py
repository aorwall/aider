import sys

MAX_RECURSION_DEPTH = 1000

def rows(row_count):
  sys.setrecursionlimit(MAX_RECURSION_DEPTH)

  if row_count < 0:
    raise ValueError("number of rows is negative")

  if row_count == 0:
    return []

  return _rows(row_count, [])

def _rows(remaining_rows, current_rows):
  if remaining_rows == 0:
    return current_rows

  first_row = [1]
  current_rows.append(first_row)

  for i in range(1, len(current_rows[-1])):
    current_rows[-1].append(current_rows[-1][i-1] + current_rows[-1][i])  

  current_rows[-1].append(1)

  return _rows(remaining_rows-1, current_rows)
