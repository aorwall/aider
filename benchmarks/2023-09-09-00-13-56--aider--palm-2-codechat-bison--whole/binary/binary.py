def parse_binary(binary_string):
  """Converts a binary number, represented as a string (e.g. '101010'), to its decimal equivalent using first principles.

  Args:
    binary_string: A string representing a binary number.

  Returns:
    The decimal equivalent of the binary number.

  Raises:
    ValueError: If the binary string is not a valid binary literal.
  """

  # Check if the binary string is a valid binary literal.
  if not binary_string.startswith("0b"):
    raise ValueError("Invalid binary literal: " + binary_string)

  # Convert the binary string to a list of digits.
  digits = binary_string[2:]

  # Convert the list of digits to a decimal number.
  decimal_number = 0
  for digit in digits:
    decimal_number = decimal_number * 2 + int(digit)

  return decimal_number
