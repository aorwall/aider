class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute
        while self.minute < 0:
            self.minute += 60
            self.hour = (self.hour - 1) % 24
        while self.minute > 59:
            self.minute -= 60
            self.hour = (self.hour + 1) % 24

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
