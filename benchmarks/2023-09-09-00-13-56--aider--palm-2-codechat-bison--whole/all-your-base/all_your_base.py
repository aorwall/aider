def rebase(input_base, digits, output_base):
  """Convert a number, represented as a sequence of digits in one base, to any other base.

  Args:
    input_base: The base of the input number.
    digits: A sequence of digits in the input base.
    output_base: The base to convert the number to.

  Returns:
    A string representing the number in the output base.

  Raises:
    ValueError: If the input base is not >= 2, or if any of the digits are not
      valid for the input base.
    ValueError: If the output base is not >= 2.
  """

  if input_base < 2:
    raise ValueError("input base must be >= 2")
  for d in digits:
    if d < 0 or d >= input_base:
      raise ValueError("all digits must satisfy 0 <= d < input base")
  if output_base < 2:
    raise ValueError("output base must be >= 2")

  # Convert the input number to a list of its digits.

  digits = list(map(int, digits))

  # Convert the number to the output base.

  result = []
  for d in digits:
    result.append(str(d))
  return "".join(result)
