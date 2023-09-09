def is_armstrong_number(number):
    number_str = str(number)
    length = len(number_str)
    sum = 0
    for digit in number_str:
        sum += int(digit)**length
    return sum == number
