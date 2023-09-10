def equilateral(sides):
  """
  Determines if a triangle is equilateral.

  An equilateral triangle has all three sides the same length.

  Args:
    sides: A list of three numbers representing the lengths of the triangle's sides.

  Returns:
    True if the triangle is equilateral, False otherwise.
  """

  # Check if all sides are the same length.
  if sides[0] == sides[1] == sides[2]:
    return True
  else:
    return False


def isosceles(sides):
  """
  Determines if a triangle is isosceles.

  An isosceles triangle has at least two sides the same length.

  Args:
    sides: A list of three numbers representing the lengths of the triangle's sides.

  Returns:
    True if the triangle is isosceles, False otherwise.
  """

  # Check if any two sides are the same length.
  if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
    return True
  else:
    return False


def scalene(sides):
  """
  Determines if a triangle is scalene.

  A scalene triangle has all sides of different lengths.

  Args:
    sides: A list of three numbers representing the lengths of the triangle's sides.

  Returns:
    True if the triangle is scalene, False otherwise.
  """

  # Check if all sides are different lengths.
  if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
    return True
  else:
    return False
