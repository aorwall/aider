import datetime
from typing import Union

def add_gigasecond(date_string: str) -> str:
    """Add a gigasecond (10^9 seconds) to the given date string in the format "yyyy-mm-dd hh:mm:ss"."""
    dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return (dt + datetime.timedelta(seconds=1e9)).strftime("%Y-%m-%d %H:%M:%S")

def add_gigasecond_using_timestamp(date_string: str) -> str:
    """Alternative implementation using timestamp."""
    ts = int(datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S").timestamp())
    giga = 1e9
    new_ts = ts + giga
    return datetime.datetime.fromtimestamp(new_ts).strftime("%Y-%m-%d %H:%M:%S")

def add_gigasecond_with_timezone(date_string: str) -> str:
    """Handling timezone aware dates."""
    from dateutil.parser import parse

    dt = parse(date_string)
    return (dt + datetime.timedelta(seconds=1e9)).isoformat()