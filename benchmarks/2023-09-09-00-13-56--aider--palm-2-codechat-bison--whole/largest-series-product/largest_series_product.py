def largest_product(series, size):
  """
  Finds the largest product of a series of adjacent digits in the input.

  Args:
    series: The sequence of digits to analyze.
    size: The length of the series to consider.

  Returns:
    The largest product of a series of adjacent digits in the input.

  Raises:
    ValueError: If the input is invalid.
  """

  # Check that the input is valid.
  if not series:
    raise ValueError("input must not be empty")
  if not isinstance(series, str):
    raise ValueError("input must be a string")
  for digit in series:
    if not digit.isdigit():
      raise ValueError("input must only contain digits")
  if size < 1:
    raise ValueError("span must not be negative")
  if size > len(series):
    raise ValueError("span must be smaller than string length")

  # Find the largest product of a series of adjacent digits.
  largest_product = 0
  for i in range(len(series) - size + 1):
    product = 1
    for j in range(size):
      product *= int(series[i + j])
    if product > largest_product:
      largest_product = product

  return largest_product
