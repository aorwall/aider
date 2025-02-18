import datetime
from calendar import monthrange

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# subclassing the built-in ValueError to create MeetupDayException

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self, message=None):
        super().__init__(message)

def check_date(year, month, day):
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        raise MeetupDayException()

def meetup(year, month, week, day_of_week):
    # Check if the input values are correct
    if year < 1900 or month > 12 or month <= 0 or week > 4 or week < 1 or day_of_week > 6 or day_of_week <= 0:
        raise MeetupDayException('Invalid input')

    # Get the last day of the month
    _, days_in_month = monthrange(year, month)

    # Calculate the first day of the month
    start_day = WEEKDAYS.index(day_of_week) - datetime.datetime(year, month, 1).weekday() + 1

    # Check if the calculated day falls within the current month
    if start_day > days_in_month:
        start_day -= 7

    # Return the nth occurence of the specified day of the week
    return start_day + (week - 1) * 7

if __name__ == '__main__':
    print(meetup(2013, 3, 1, 'Tuesday'))
