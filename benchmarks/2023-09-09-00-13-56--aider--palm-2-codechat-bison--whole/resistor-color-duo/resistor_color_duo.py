def value(colors):
  """
  Takes a list of color names and returns the corresponding two-digit value.

  >>> value(['brown', 'green'])
  15
  >>> value(['brown', 'green', 'violet'])
  15

  Args:
    colors: A list of color names.

  Returns:
    A two-digit integer representing the value of the resistor.
  """

  # First, we need to convert the color names to numbers.
  # We can do this using a dictionary.

  color_codes = {
      'black': 0,
      'brown': 1,
      'red': 2,
      'orange': 3,
      'yellow': 4,
      'green': 5,
      'blue': 6,
      'violet': 7,
      'grey': 8,
      'white': 9,
  }

  # Now, we need to multiply each color code by its position.
  # The first color is multiplied by 10, and the second color is multiplied by 1.

  value = 0
  for i, color in enumerate(colors):
    value += color_codes[color] * (10 ** i)

  # Finally, we need to return the value.

  return value
