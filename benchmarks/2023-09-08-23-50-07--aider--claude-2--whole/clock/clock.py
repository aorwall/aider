class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        new_minute = (self.minute + minutes) % 60
        new_hour = (self.hour + (self.minute + minutes) // 60) % 24
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        return self.__add__(-minutes)
