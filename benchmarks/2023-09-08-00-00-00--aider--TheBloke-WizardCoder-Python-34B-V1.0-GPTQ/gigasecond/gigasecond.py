import datetime

def add_gigasecond(birth_date):
    return birth_date + datetime.timedelta(seconds=1e9)

def add_gigasecond_with_input_validation(birth_date_input):
    try:
        birth_date = datetime.datetime.strptime(birth_date_input, "%m/%d/%Y %H:%M:%S")
        return add_gigasecond(birth_date)
    except ValueError:
        raise ValueError("Incorrect date format, should be MM/DD/YYYY HH:MM:SS")

if __name__ == "__main__":
    birth_date_input = input("Enter your birth date (MM/DD/YYYY HH:MM:SS): ")
    try:
        birth_date = datetime.datetime.strptime(birth_date_input, "%m/%d/%Y %H:%M:%S")
        one_gigasecond_later = add_gigasecond(birth_date)
        print("One gigasecond after your birth date is:", one_gigasecond_later.strftime("%m/%d/%Y %H:%M:%S"))
    except ValueError:
        print("Incorrect date format, should be MM/DD/YYYY HH:MM:SS")
