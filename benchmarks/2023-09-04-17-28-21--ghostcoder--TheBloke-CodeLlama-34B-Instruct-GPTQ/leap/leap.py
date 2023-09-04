def leap_year(year):
    """Return True if year is a leap year, False otherwise."""
    # Check if year is divisible by 4
    if year % 4 != 0:
        return False
    # Check if year is divisible by 100
    elif year % 100 != 0:
        return True
    # Check if year is divisible by 400
    elif year % 400 != 0:
        return False
    else:
        return True
