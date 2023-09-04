def leap_year(year):
    if (year % 4) != 0:
        # Year is not a leap year if it is not divisible by 4
        return False
    elif (year % 100) != 0:
        # Year is a leap year if it is divisible by 4 and not by 100
        return True
    elif (year % 400) != 0:
        # Year is not a leap year if it is divisible by 100 but not by 400
        return False
    else:
        # Otherwise, year is a leap year
        return True
