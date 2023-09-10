def leap_year(year):
  """
  Determines if the given year is a leap year.

  A leap year in the Gregorian calendar occurs:

  * on every year that is evenly divisible by 4
  * except every year that is evenly divisible by 100
  * unless the year is also evenly divisible by 400

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """

  # Check if the year is evenly divisible by 4.
  if year % 4 == 0:
    # Check if the year is evenly divisible by 100.
    if year % 100 == 0:
      # Check if the year is also evenly divisible by 400.
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
