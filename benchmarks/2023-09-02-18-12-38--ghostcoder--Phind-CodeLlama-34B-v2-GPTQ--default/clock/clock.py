class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.hour == other.hour and self.minute == other.minute
        else:
            return False

    def __add__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute) + minutes
        new_clock = Clock(*divmod(total_minutes, 60))
        return new_clock

    def __sub__(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative")

        total_minutes = (self.hour * 60 + self.minute) - minutes
        new_clock = Clock(*divmod(total_minutes, 60))
        return new_clock
