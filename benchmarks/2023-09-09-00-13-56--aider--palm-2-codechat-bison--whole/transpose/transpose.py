def transpose(lines):
  """
  Transposes a matrix of strings.

  Args:
    lines: A list of strings, where each string is a row in the matrix.

  Returns:
    A list of strings, where each string is a column in the transposed matrix.
  """

  # Pad each row to the same length.
  max_length = max(len(line) for line in lines)
  for line in lines:
    line += ' ' * (max_length - len(line))

  # Transpose the matrix.
  transposed_lines = []
  for i in range(max_length):
    transposed_line = ''
    for line in lines:
      transposed_line += line[i]
    transposed_lines.append(transposed_line)

  return transposed_lines
