from datetime import datetime, timedelta

def add(moment):
    gigasecond = timedelta(seconds=10**9)
    return moment + gigasecond