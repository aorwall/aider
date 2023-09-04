class Clock:
    def __init__(self, hour, minute):
        self.hour = (hour % 24 + minute // 60) % 24
        self.minute = minute % 60


    def __repr__(self):
        return f"<Clock {self.hour} {self.minute}" # Use f-string here


    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}".format(self.hour, self.minute) # Use proper formating 


    def __eq__(self, other):
        return isinstance(other, Clock) and self.hour == other.hour and self.minute == other.minute


    def __add__(self, minutes):
        return Clock((self.hour + minutes // 60) % 24, self.minute + minutes % 60)


    def __sub__(self, minutes):
        mins_diff = self.minute - minutes
        if mins_diff < 0:
            return Clock((self.hour - 1) % 24, mins_diff + 60)
        else:
            return Clock(self.hour, mins_diff)
