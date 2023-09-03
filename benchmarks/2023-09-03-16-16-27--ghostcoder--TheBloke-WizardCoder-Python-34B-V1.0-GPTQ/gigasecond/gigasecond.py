from datetime import timedelta
import re

def add(moment):
    match = re.match("^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}:)(\d{2})$", moment)
    if not match:
        raise ValueError("Invalid date format")
    year, month, day, hour, minute, second = map(int, match.groups())
    return (datetime.datetime(year, month, day, hour, minute, second) + 
            timedelta(seconds=1e9))
