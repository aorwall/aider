from datetime import datetime, timedelta
from datetime import timedelta
import re

def add_gigasecond(dt):
    return dt + timedelta(seconds=1e9)

def add_gigasecond(moment):
    return moment + timedelta(seconds=1e9)

def parse_date_time(input_string):
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    match = re.search(pattern, input_string)

    if not match:
        raise ValueError("Invalid input string format")

    parsed_string = match.group()
    formatted_string = f"{parsed_string}.000000"
    return datetime.strptime(formatted_string, "%Y-%m-%d %H:%M:%S.%f")

if __name__ == '__main__':
    input_string = input('Enter a date and time in yyyy-mm-dd hh:mm:ss format: ')
    try:
        formatted_datetime = parse_date_time(input_string)
        result = add_gigasecond(formatted_datetime)
        print(result.isoformat())
    except ValueError as ve:
        print(ve)