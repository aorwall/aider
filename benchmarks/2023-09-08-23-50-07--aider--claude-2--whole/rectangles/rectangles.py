def rectangles(strings):
  count = 0
  
  for row in range(len(strings)):
    for col in range(len(strings[row])):
      if strings[row][col] == '+':
        # Found top left corner, check if a rectangle
        if row+1 < len(strings) and col+1 < len(strings[row]) and strings[row+1][col] == '|' and strings[row][col+1] == '-':
          count += 1
        elif row+1 < len(strings) and strings[row+1][col] == '+':
          count += 1
  
  return count
