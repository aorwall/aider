import datetime
from typing import Optional

WEEKDAYS = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    
    message: explanation of the error.
    
    """
    def __init__(self, message="Invalid weekday and count combination."):
        super().__init__(message)


def meetup(year: int, month: int, week: str, day_of_week: str) -> Optional[datetime.date]:
    try:
        # Convert input strings to integer values
        year = int(year)
        month = int(month)

        # Get the index of the first weekday of the desired week
        week_index = WEEKDAYS.get(int(day_of_week[-1]))
        if week_index is None:
            raise KeyError("Invalid day of the week")

        start_date = datetime.date(year=year, month=month, day=1)
        while True:
            if start_date.strftime("%A").startswith(week[:3]):
                break

            start_date += datetime.timedelta(days=1)

        match_dates = []
        for i in range(len([i for i in range(start_date.day - 1, 31)])):
            test_date = start_date + datetime.timedelta(days=i)
            if test_date.isocalendar()[1] == week_index:
                match_dates.append(test_date)

        return match_dates[int(week)-1]

    except (KeyError, IndexError, ValueError) as e:
        raise MeetupDayException(f"{e}. Please provide a valid week value between 1 and 4, and a valid day of the week value between 1 and 7.")


def meetup(year, month, week, day_of_week):
    pass
