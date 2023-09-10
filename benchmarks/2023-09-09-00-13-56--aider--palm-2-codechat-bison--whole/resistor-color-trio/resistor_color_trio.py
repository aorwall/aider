def label(colors):
  """
  This function takes in a list of three colors and returns a label for the resistor.
  The colors are encoded as follows:

  - Black: 0
  - Brown: 1
  - Red: 2
  - Orange: 3
  - Yellow: 4
  - Green: 5
  - Blue: 6
  - Violet: 7
  - Grey: 8
  - White: 9

  The first two colors represent the main value of the resistor.
  The third color represents the number of zeros to add to the main value.

  For example, an input of `"orange", "orange", "black"` would return a label of "33 ohms".

  When we get to larger resistors, a [metric prefix](https://en.wikipedia.org/wiki/Metric_prefix) is used to indicate a larger magnitude of ohms, such as "kiloohms".
  That is similar to saying "2 kilometers" instead of "2000 meters", or "2 kilograms" for "2000 grams".

  For example, an input of `"orange", "orange", "orange"` would return a label of "33 kiloohms".

  Args:
    colors: A list of three colors.

  Returns:
    A label for the resistor.
  """

  # Convert the colors to numbers.
  main_value = int(colors[0]) * 10 + int(colors[1])

  # Get the number of zeros to add.
  zeros = int(colors[2])

  # Calculate the final value.
  final_value = main_value * (10 ** zeros)

  # Get the appropriate metric prefix.
  prefix = "ohms"
  if final_value >= 1000:
    prefix = "kiloohms"
  elif final_value >= 1000000:
    prefix = "megaohms"
  elif final_value >= 1000000000:
    