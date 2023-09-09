def square_of_sum(number):
    sum_of_numbers = 0
    for i in range(1, number+1):
        sum_of_numbers += i
    return sum_of_numbers ** 2


def sum_of_squares(number):
    sum_of_squares = 0
    for i in range(1, number+1):
        sum_of_squares += i ** 2
    return sum_of_squares


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
