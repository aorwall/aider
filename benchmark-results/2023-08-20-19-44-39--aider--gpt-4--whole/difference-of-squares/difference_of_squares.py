def square_of_sum(number):
    # The square of the sum of the first N natural numbers can be calculated using the formula: ((N*(N+1))/2)^2
    return ((number*(number+1))//2)**2


def sum_of_squares(number):
    # The sum of the squares of the first N natural numbers can be calculated using the formula: (N*(N+1)*(2N+1))/6
    return (number*(number+1)*(2*number+1))//6


def difference_of_squares(number):
    # The difference between the square of the sum and the sum of the squares of the first N natural numbers
    return square_of_sum(number) - sum_of_squares(number)
