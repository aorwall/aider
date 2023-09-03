import calendar
from datetime import timedelta, datetime
from datetime import timedelta

DAYS_OF_WEEK = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}
# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    
    message: explanation of the error.
    
    """
    def __init__(self, message=""):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    try:
        # Check if the given day_of_week is valid
        if day_of_week not in DAYS_OF_WEEK:
            raise MeetupDayException('Invalid Day')

        # Get the last day of the month
        _, last_day = calendar.monthrange(year, month)

        # Calculate the first possible date for the given weekday
        first_date = DAYS_OF_WEEK[day_of_week] - (week - 1) % 5
        if first_date >= 7:
            first_date -= 7

        # Create a date object for the calculated date
        current_date = timedelta(days=first_date - 1) + datetime(year, month, 1).replace(day=1)

        # Add weeks to the initial date until we get to the correct week
        while current_date.isocalendar()[1] != week:
            current_date += timedelta(weeks=1)

        return current_date.date().isoformat()

    except Exception as e:
        raise MeetupDayException("That day does not exist.") from e
