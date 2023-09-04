def leap_year(year):
    """Return True if `year` is a leap year, False otherwise."""
    if year % 4 != 0:
        # Not a leap year if not divisible by 4
        return False
    elif year % 100 != 0:
        # Leap year if divisible by 4 but not by 100
        return True
    else:
        # If divisible by both 4 and 100, must also be divisible by 400
        return year % 400 == 0
