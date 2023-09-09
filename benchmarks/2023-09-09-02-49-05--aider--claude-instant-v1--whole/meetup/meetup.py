# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    import calendar
    
    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    
    cal = calendar.monthcalendar(year, month)
    
    if week == "last":
        for i in range(-1, -8, -1):
            date = cal[i][days[day_of_week]]
            if date != 0:
                return f"{month}/{date}/{year}"
        raise MeetupDayException(f"There is no {day_of_week} in the last week of {month} {year}.")
        
    elif week == "teenth":
        for i in range(0, 3):
            for j in range(0, 7):
                if 13 <= cal[i][j] <= 19:
                    return f"{month}/{cal[i][j]}/{year}"
        raise MeetupDayException(f"There is no {day_of_week} ending in '-teen' in {month} {year}.")
        
    elif week == "fifth":
        count = 0
        for i in range(len(cal)-1, -1, -1):
            for j in range(len(cal[i])):
                if cal[i][j] != 0:
                    count += 1
                    if count > 5:
                        return f"{month}/{cal[i][j]}/{year}"
        raise MeetupDayException(f"There is no fifth {day_of_week} in {month} {year}.")
        
    else:
        week = int(week) - 1
        date = cal[week][days[day_of_week]]
        if date == 0:
            raise MeetupDayException(f"There is no {day_of_week} in the {week+1} week of {month} {year}.")
        return f"{month}/{date}/{year}"
