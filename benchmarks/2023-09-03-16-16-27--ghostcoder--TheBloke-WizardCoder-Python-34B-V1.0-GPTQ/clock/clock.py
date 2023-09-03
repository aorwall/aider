from datetime import datetime
import datetime

class Clock:
    def __init__(self, hour=None, minute=None):
        self._hour = None
        self._minute = None

        # If both arguments are provided, set them directly.
        if hour is not None and minute is not None:
            self._set_time(hour, minute)
        else:
            now = datetime.now()
            self._set_time(now.hour, now.minute)


    def _set_time(self, hour, minute):
        """Set the time using hours and minutes."""
        self._hour = hour % 24
        self._minute = minute % 60

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_mins = self.minute + minutes
        extra_hours = int(total_mins // 60)
        new_hour = (self.hour + extra_hours) % 24
        new_minutes = total_mins % 60
        return Clock(new_hour, new_minutes)

    def __sub__(self, minutes):
        total_mins = self.minute - minutes
        if total_mins >= 0:
            return Clock(self.hour, total_mins)
        else:
            new_hour = (self.hour - 1) % 24
            new_minutes = abs(total_mins) % 60
            return Clock(new_hour, new_minutes)
