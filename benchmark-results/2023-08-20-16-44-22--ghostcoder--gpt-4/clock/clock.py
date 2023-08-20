class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        self.minutes = total_minutes % 60
        self.hours = (total_minutes // 60) % 24

    def __repr__(self):
        return f"Clock({self.hours}, {self.minutes})"

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)