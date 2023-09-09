def spiral_matrix(size):
  matrix = [[0 for x in range(size)] for y in range(size)]

  num = 1
  top = 0
  bottom = size - 1
  left = 0 
  right = size - 1

  while num <= size * size:
    for i in range(left, right + 1):
      matrix[top][i] = num
      num += 1
    top += 1

    for i in range(top, bottom + 1):
      matrix[i][right] = num  
      num += 1
    right -= 1

    for i in range(right, left - 1, -1):
      matrix[bottom][i] = num
      num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
      matrix[i][left] = num
      num += 1
    left += 1

  return matrix
