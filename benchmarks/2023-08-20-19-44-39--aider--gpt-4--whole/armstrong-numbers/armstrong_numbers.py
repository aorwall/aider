def is_armstrong_number(number):
    str_number = str(number)
    power = len(str_number)
    sum_of_digits = sum(int(digit) ** power for digit in str_number)
    return sum_of_digits == number
