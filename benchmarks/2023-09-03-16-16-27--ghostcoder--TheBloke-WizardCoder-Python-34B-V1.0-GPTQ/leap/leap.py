def leap_year(year):
    """Return True if year is a leap year, False otherwise."""
    if year % 4 == 0:
        if year % 100 != 0:
            # If the year is divisible by 4 but not by 100, it is a leap year
            return True
        elif year % 400 == 0:
            # If the year is divisible by both 4 and 100, it is a leap year only if it is also divisible by 400
            return True
        else:
            # Otherwise, it is not a leap year
            return False
    else:
        return False
