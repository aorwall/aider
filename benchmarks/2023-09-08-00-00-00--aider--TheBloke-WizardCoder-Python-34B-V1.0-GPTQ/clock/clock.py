class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def add_minutes(self, minutes):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        self.hour %= 24

    def subtract_minutes(self, minutes):
        self.minute -= minutes
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        self.hour %= 24
