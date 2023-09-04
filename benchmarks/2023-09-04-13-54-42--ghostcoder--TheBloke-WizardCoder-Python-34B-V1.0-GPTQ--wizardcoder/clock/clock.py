import datetime
from typing import Union

class Clock:
    def __init__(self, hour: int, minute: int):
        self._hour = hour % 24
        self._minute = minute % 60

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.hour}, {self.minute})"

    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: 'Clock') -> bool:
        return (isinstance(other, type(self)) and
                self.hour == other.hour and
                self.minute == other.minute)

    def __add__(self, minutes: int) -> 'Clock':
        total_minutes = self.minute + minutes

        extra_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        new_hour = (self.hour + extra_hours) % 24
        new_minute = remaining_minutes

        return Clock(new_hour, new_minute)

    def __sub__(self, minutes: int) -> 'Clock':
        return self + (-minutes)

def parse_clock(input_value: Union[str, tuple]) -> Clock:
    if isinstance(input_value, str):
        input_values = input_value.split(":")
        hours, minutes = map(int, input_values)
    elif isinstance(input_value, tuple):
        hours, minutes = input_value
    else:
        raise ValueError("Invalid input value.")

    return Clock(hours, minutes)
