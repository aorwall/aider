def parse_octal(digits):
  """Converts an octal number, represented as a string, to its decimal equivalent.

  Args:
    digits: A string representing an octal number.

  Returns:
    The decimal equivalent of the octal number.

  Raises:
    ValueError: If the input string is not a valid octal number.
  """

  # Check if the input string is a valid octal number.
  if not digits.isdigit() or digits[0] != '0':
    raise ValueError('Invalid octal number: {}'.format(digits))

  # Convert the octal number to a list of digits.
  digits = list(digits)

  # Initialize the result.
  result = 0

  # Iterate over the digits from right to left.
  for i in range(len(digits) - 1, -1, -1):
    # Multiply the current digit by the appropriate power of 8.
    digit = int(digits[i])
    exponent = len(digits) - 1 - i
    value = digit * 8 ** exponent

    # Add the current value to the result.
    result += value

  # Return the result.
  return result
