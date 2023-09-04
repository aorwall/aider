import datetime
from calendar import monthrange

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# subclassing the built-in ValueError to create MeetupDayException

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self, message=None):
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    try:
        assert week in range(1, 5), f"Week {week} out of bounds. Must be within 1..4."
        assert day_of_week in WEEKDAYS, f"Invalid day of week '{day_of_week}'."

        first_day, last_day = monthrange(year, month)[0], monthrange(year, month)[1]
        start_date = datetime.datetime(year, month, 1) + datetime.timedelta(days=(week - 1) * 7)
        end_date = start_date + datetime.timedelta(weeks=1)

        while start_date <= end_date:
            if start_date.strftime('%A') == day_of_week:
                return start_date.day

            start_date += datetime.timedelta(days=1)

        raise MeetupDayException(f"No {day_of_week} found in {month}/{year}.")
    except AssertionError as e:
        raise MeetupDayException(e)
