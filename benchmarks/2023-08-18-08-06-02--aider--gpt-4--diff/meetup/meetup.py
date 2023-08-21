import calendar

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    # Convert day_of_week to a number
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_num = days.index(day_of_week)

    # Get the month's calendar
    month_cal = calendar.monthcalendar(year, month)

    # Find the correct day
    if week == 'teenth':
        for i in [1, 2]:  # second and third weeks
            if month_cal[i][day_num] != 0:
                return year, month, month_cal[i][day_num]
    elif week == 'last' or week == 'fifth':
        for i in reversed(range(len(month_cal))):  # last week
            if month_cal[i][day_num] != 0:
                if week == 'last' or (week == 'fifth' and i == 4):
                    return year, month, month_cal[i][day_num]
    else:
        week_num = ['first', 'second', 'third', 'fourth'].index(week)
        if month_cal[week_num][day_num] != 0:
            return year, month, month_cal[week_num][day_num]

    # If no valid day was found, raise an exception
    raise MeetupDayException("That day does not exist.")
