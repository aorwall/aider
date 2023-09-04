from datetime import datetime, timedelta

def add(moment):
    return moment + timedelta(seconds=10**9)

if __name__ == '__main__':
    birthday = datetime(2015, 1, 24, 22, 0)
    print("Birthday: ", birthday)
    giga_birthday = add(birthday)
    print("Gigasecond Anniversary: ", giga_birthday)
