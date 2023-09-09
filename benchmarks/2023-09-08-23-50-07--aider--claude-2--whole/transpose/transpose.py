def transpose(lines):
  transposed = []
  
  if not lines:
    return transposed

  num_rows = len(lines)
  max_cols = max(len(line) for line in lines)
  
  for col in range(max_cols):
    new_row = ""
    for row in range(num_rows):
      if col < len(lines[row]):
        new_row += lines[row][col]
      else:
        new_row += " "
    transposed.append(new_row)
  
  return transposed
