class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.hour == other.hour and self.minute == other.minute
        else:
            return False

    def __add__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute) + minutes
        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return Clock(extra_hours, remaining_minutes)

    def __sub__(self, minutes):
        total_minutes = (self.hour * 60 + self.minute) - minutes
        if total_minutes < 0:
            raise ValueError("Resulting time cannot be negative")

        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return Clock(extra_hours, remaining_minutes)
