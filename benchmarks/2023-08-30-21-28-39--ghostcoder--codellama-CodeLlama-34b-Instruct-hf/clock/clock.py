class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        if self.minute >= 60:
            self.hour += 1
            self.minute -= 60
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        if self.minute < 0:
            self.hour -= 1
            self.minute += 60
        return self
