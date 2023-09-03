class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        extra_hours = total_minutes // 60
        new_hour = (self.hour + extra_hours) % 24
        new_minute = total_minutes % 60
        if new_minute < 0:
            new_hour -= 1
            new_minute += 60
        return Clock(new_hour, abs(new_minute))

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes
        if total_minutes < 0:
            new_hour = (self.hour - 1) % 24
            new_minute = total_minutes % 60 + 60
        else:
            new_hour = self.hour
            new_minute = total_minutes
        return Clock(new_hour, abs(new_minute))
