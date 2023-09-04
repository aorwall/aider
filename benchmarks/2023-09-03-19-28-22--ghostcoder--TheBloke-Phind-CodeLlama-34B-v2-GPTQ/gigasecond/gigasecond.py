from datetime import datetime, timedelta


def add(moment):
    # Add one gigasecond, which is equal to one billion seconds
    return moment + timedelta(seconds=1e9)
