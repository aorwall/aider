class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour}:{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        minutes += self.minute
        hours = minutes // 60
        minutes %= 60
        self.hour += hours
        self.minute = minutes
        return self

    def __sub__(self, minutes):
        minutes = self.minute - minutes
        hours = minutes // 60
        minutes %= 60
        self.hour -= hours
        self.minute = minutes
        return self
