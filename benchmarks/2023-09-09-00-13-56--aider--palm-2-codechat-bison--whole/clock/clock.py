class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.hour == other.hour and self.minute == other.minute
        return False

    def __add__(self, minutes):
        new_hour = self.hour + (minutes // 60)
        new_minute = self.minute + (minutes % 60)
        if new_minute >= 60:
            new_hour += 1
            new_minute -= 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        new_hour = self.hour - (minutes // 60)
        new_minute = self.minute - (minutes % 60)
        if new_minute < 0:
            new_hour -= 1
            new_minute += 60
        return Clock(new_hour, new_minute)
