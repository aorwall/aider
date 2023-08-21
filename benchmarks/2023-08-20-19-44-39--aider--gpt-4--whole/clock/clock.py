class Clock:
    def __init__(self, hour, minute):
        self.minutes = (hour * 60 + minute) % 1440

    def __repr__(self):
        return f"Clock({self.minutes // 60}, {self.minutes % 60})"

    def __str__(self):
        return f"{self.minutes // 60:02d}:{self.minutes % 60:02d}"

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
