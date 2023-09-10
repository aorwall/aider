def square(number):
  """
  Calculates the number of grains of wheat on a chessboard given the square number.

  Args:
    number: The square number.

  Returns:
    The number of grains of wheat on the given square.

  Raises:
    ValueError: When the square number is not in the range of 1 to 64.
  """

  if number < 1 or number > 64:
    raise ValueError("square must be between 1 and 64")

  # Calculate the number of grains of wheat on the given square.

  grains = 1
  for i in range(1, number + 1):
    grains *= 2

  return grains


def total():
  """
  Calculates the total number of grains of wheat on a chessboard.

  Returns:
    The total number of grains of wheat on the chessboard.
  """

  return square(64)
