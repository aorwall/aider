class Clock:
    def __init__(self, hour, minute):
        self._hour = hour
        self._minute = minute

    def __repr__(self):
        return f"{self.__class__.__name__}({self._hour}, {self._minute})"

    def __str__(self):
        return f"{self._hour:02d}:{self._minute:02d}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        total_minutes = self._hour * 60 + self._minute + minutes
        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return Clock(extra_hours, remaining_minutes)

    def __sub__(self, minutes):
        total_minutes = self._hour * 60 + self._minute - minutes
        if total_minutes < 0:
            raise ValueError("Minutes subtraction result cannot be negative.")

        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        return Clock(extra_hours, remaining_minutes)
