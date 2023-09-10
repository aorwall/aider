def is_valid(isbn):
  """
  Determines if the given ISBN-10 is valid.

  Args:
    isbn: A string containing the ISBN-10.

  Returns:
    True if the ISBN-10 is valid, False otherwise.
  """

  # Check if the ISBN-10 is in the correct format.
  if not isbn.isdigit():
    return False
  if len(isbn) != 10:
    return False

  # Convert the ISBN-10 to a list of digits.
  digits = list(map(int, isbn))

  # Calculate the check digit.
  check_digit = 0
  for i in range(10):
    check_digit += digits[i] * (10 - i)
  check_digit %= 11
  if check_digit == 10:
    check_digit = 0

  # Check if the check digit is correct.
  if digits[-1] != check_digit:
    return False

  # The ISBN-10 is valid.
  return True
