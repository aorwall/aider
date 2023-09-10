def spiral_matrix(size):
  """
  Given the size, return a square matrix of numbers in spiral order.

  The matrix should be filled with natural numbers, starting from 1 in the top-left corner, increasing in an inward, clockwise spiral order, like these examples:

  ## Examples

  ### Spiral matrix of size 3

  ```text
  1 2 3
  8 9 4
  7 6 5
  ```

  ### Spiral matrix of size 4

  ```text
  1  2  3  4
 12 13 14  5
 11 16 15  6
 10  9  8  7
  ```

  """

  # Initialize the matrix.
  matrix = [[0] * size for _ in range(size)]

  # Start at the top-left corner and move in an inward, clockwise spiral order.
  i = 0
  j = 0
  direction = 1  # 1 = right, 2 = down, 3 = left, 4 = up

  while i < size and j < size:
    # Place the current number in the matrix.
    matrix[i][j] = i * size + j + 1

    # Move to the next position.
    if direction == 1:
      if j + 1 < size:
        j += 1
      else:
        direction = 2
        i += 1
    elif direction == 2:
      if i + 1 < size:
        i += 1
      else:
        direction = 3
        j -= 1
    elif direction == 3:
      if j - 1 >= 0:
        j -= 1
      else:
        direction = 4
        i -= 1
    else:
      if i - 1 >= 0:
        i -= 1
      else:
        direction = 1
        j += 1

  return matrix
