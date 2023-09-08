# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

def meetup(year, month, week, day_of_week):
    # Your code here
    pass

# raise a MeetupDayException
raise MeetupDayException("That day does not exist.")
