from datetime import date

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    # Get the first day of the month
    first_day = date(year, month, 1)

    # Get the weekday of the first day
    first_day_weekday = first_day.weekday()

    # Convert day_of_week to an integer
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week)

    # Calculate the offset to the desired weekday
    offset = (day_of_week - first_day_weekday) % 7

    # Calculate the date of the meetup
    meetup_date = first_day.day + offset

    # Check if the meetup date is valid
    if meetup_date > 31:
        raise MeetupDayException("That day does not exist.")

    return meetup_date