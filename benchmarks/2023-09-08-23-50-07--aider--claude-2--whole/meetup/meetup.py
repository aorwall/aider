# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    import calendar
    import datetime
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day_of_week not in days_of_week:
        raise MeetupDayException(f"{day_of_week} is not a valid day of the week.")
    
    week_numbers = ['first', 'second', 'third', 'fourth', 'last', 'teenth']
    if week not in week_numbers:
        raise MeetupDayException(f"{week} is not a valid week number.")
    
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    month_weekdays = [day for day in month_days if day != 0]
    month_weekdays_in_days = [datetime.date(year, month, day).weekday() for day in month_weekdays]
    
    target_weekday = days_of_week.index(day_of_week)
    
    if week == 'first':
        target_day = month_weekdays[month_weekdays_in_days.index(target_weekday)]
    elif week == 'second':
        target_day = month_weekdays[month_weekdays_in_days.index(target_weekday, 
                                                              month_weekdays_in_days.index(target_weekday)+1)]
    elif week == 'third':
        target_day = month_weekdays[month_weekdays_in_days.index(target_weekday,
                                                              month_weekdays_in_days.index(target_weekday,
                                                                                          month_weekdays_in_days.index(target_weekday)+1)+1)]
    elif week == 'fourth':
        target_day = month_weekdays[month_weekdays_in_days.index(target_weekday,
                                                                month_week