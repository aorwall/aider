def color_code(color):
  """Returns the numerical value associated with a particular color band.

  Args:
    color: The color of the band as a string.

  Returns:
    The numerical value associated with the color.
  """

  # Create a lookup table for the colors.
  colors = {
      "black": 0,
      "brown": 1,
      "red": 2,
      "orange": 3,
      "yellow": 4,
      "green": 5,
      "blue": 6,
      "violet": 7,
      "grey": 8,
      "white": 9,
  }

  # Return the numerical value for the given color.
  return colors[color]


def colors():
  """Returns a list of all the different band colors.

  Returns:
    A list of all the different band colors.
  """

  # Return a list of all the colors in the lookup table.
  return list(colors.keys())
