import datetimeimport calendar
from datetime import date
from typing import Union

class MeetupDayException(Exception):
    pass

def meetup_day(year: int, month: int, day_of_week: str, week: int) -> datetime.date:
    """Returns the date of a meetup given year, month, day of week and week number."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        weekday_number = days.index(day_of_week.title()) + 1 # get index of day of week (0 based)
    except ValueError:
        raise MeetupDayException()

    if week < 1 or week > 5:
        raise MeetupDayException("Week must be between 1 and 5")

    num_days = calendar.monthrange(year, month)[1]
    if week == 5:
        return datetime.date(year, month, num_days - ((num_days % 7) + 2))
    elif week == 1:
        return datetime.date(year, month, weekday_number)
    else:
        return datetime.date(year, month, weekday_number + (week-1)*7 + (weekday_number <= 4))

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Invalid weekday or count provided."):
        super().__init__(message)

def meetup(year, month, week, day_of_week):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        weekday_number = days.index(day_of_week.title()) + 1 # get index of day of week (0 based) and add 1 since Monday is 1
    except ValueError:
        raise MeetupDayException()

    if week < 1 or week > 5:
        raise MeetupDayException("Week must be between 1 and 5")

    num_days = calendar.monthrange(year, month)[1]
    if week == 5:
        return datetime.date(year, month, num_days - ((num_days % 7) + 2))
    elif week == 1:
        return datetime.date(year, month, weekday_number)
    else:
        return datetime.date(year, month, weekday_number + (week-1)*7 + (weekday_number <= 4))