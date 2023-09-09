import datetime

def add(moment):
    gigasecond = datetime.timedelta(seconds=10**9)
    return moment + gigasecond
