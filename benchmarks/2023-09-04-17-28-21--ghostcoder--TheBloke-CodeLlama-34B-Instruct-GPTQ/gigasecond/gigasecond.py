import datetime

def add(moment):
    return moment + datetime.timedelta(seconds = int(1e9))
