import math

def square_of_sum(number):
    return int((math.pow((number * (number + 1)) / 2, 2)))


def sum_of_squares(number):
    total = 0
    for num in range(1, number + 1):
        total += math.pow(num, 2)
    return total


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
