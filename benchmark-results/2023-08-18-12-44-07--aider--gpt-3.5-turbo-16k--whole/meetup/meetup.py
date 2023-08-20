from datetime import date, timedelta

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

    # Calculate the weekday of the first day (Monday = 0, Sunday = 6)
    first_weekday = first_day.weekday()

    # Calculate the target weekday (Monday = 0, Sunday = 6)
    target_weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day_of_week)

    # Calculate the number of days to the target weekday
    days_to_target = (target_weekday - first_weekday) % 7

    # Calculate the date of the first occurrence of the target weekday
    first_occurrence = first_day + timedelta(days=days_to_target)

    # Calculate the date of the last occurrence of the target weekday
    last_occurrence = first_occurrence + timedelta(weeks=1)

    # Calculate the date of the desired occurrence based on the week parameter
    if week == "teenth":
        # Find the first occurrence that falls between 13th and 19th of the month
        while first_occurrence.day < 13 or first_occurrence.day > 19:
            first_occurrence += timedelta(weeks=1)
        return first_occurrence
    elif week == "last":
        # Find the last occurrence of the target weekday in the month
        while last_occurrence.month == month:
            last_occurrence += timedelta(weeks=1)
        return last_occurrence - timedelta(weeks=1)
    else:
        # Find the nth occurrence of the target weekday in the month
        nth_occurrence = int(week[0]) - 1
        desired_occurrence = first_occurrence + timedelta(weeks=nth_occurrence)
        if desired_occurrence.month != month:
            raise MeetupDayException("Invalid date")
        return desired_occurrence
