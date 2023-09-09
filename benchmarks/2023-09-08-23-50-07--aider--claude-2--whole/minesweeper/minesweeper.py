def annotate(minefield):
  # Function body starts here
  if isinstance(minefield, list):
    minefield = '\n'.join(minefield)
  
  rows = minefield.split('\n')
  height = len(rows)
  width = len(rows[0])

  if any(len(row) != width for row in rows):
    raise ValueError('The board is not rectangular.')

  annotated = []
  for y, row in enumerate(rows):
    annotated_row = []
    for x, cell in enumerate(row):
      if cell == '*':
        continue
      count = 0
      for dy in range(-1, 2):
        for dx in range(-1, 2):
          if dy == 0 and dx == 0:
            continue
          ny = y + dy
          nx = x + dx
          if 0 <= ny < height and 0 <= nx < width:
            if rows[ny][nx] == '*':
              count += 1
      annotated_row.append(str(count) if count > 0 else ' ')
    annotated.append(''.join(annotated_row))
  
  return '\n'.join(annotated)
