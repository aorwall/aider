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

    def __add__(self, minutes):
        total_minutes = self.hour * 60 + self.minute + minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)

    def __sub__(self, minutes):
        total_minutes = self.hour * 60 + self.minute - minutes
        new_hour = (total_minutes // 60) % 24
        new_minute = total_minutes % 60
        return Clock(new_hour, new_minute)
