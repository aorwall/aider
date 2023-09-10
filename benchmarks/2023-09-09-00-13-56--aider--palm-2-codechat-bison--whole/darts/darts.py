def score(x, y):
  """
  Returns the earned points in a single toss of a Darts game.

  Args:
    x: The x-coordinate of the dart landing.
    y: The y-coordinate of the dart landing.

  Returns:
    The number of points earned by the dart.
  """

  # Calculate the distance from the dart landing to the center of the target.
  distance = ((x ** 2) + (y ** 2)) ** 0.5

  # If the dart lands outside the target, return 0 points.
  if distance > 10:
    return 0

  # Otherwise, return the appropriate number of points based on the dart's distance from the center of the target.
  if distance <= 1:
    return 10
  elif distance <= 5:
    return 5
  else:
    return 1
