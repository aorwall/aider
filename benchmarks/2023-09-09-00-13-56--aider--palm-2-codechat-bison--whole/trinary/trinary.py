def trinary(string):
  """Converts a trinary number to its decimal equivalent.

  Args:
    string: A string representing a trinary number.

  Returns:
    The decimal equivalent of the trinary number.
  """

  if not string:
    return 0

  # Initialize the result.
  result = 0

  # Iterate over the string from right to left.
  for i in range(-len(string), 0):
    # Get the value of the current digit.
    digit = int(string[i])

    # Multiply the result by 3 and add the value of the current digit.
    result *= 3
    result += digit

  return result
