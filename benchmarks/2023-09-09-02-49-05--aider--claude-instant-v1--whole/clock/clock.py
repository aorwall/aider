from math import floor

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.hour == other.hour and self.minute == other.minute
        else:
            return False

    def __add__(self, minutes):
        total_minutes = self.hour * 60 + self.minute + minutes
        hours = floor(total_minutes / 60)
        minutes = total_minutes % 60
        return Clock(hours, minutes)

    def __sub__(self, minutes):
        total_minutes = self.hour * 60 + self.minute - minutes
        hours = floor(total_minutes / 60)
        minutes = total_minutes % 60
        return Clock(hours, minutes)
