import math

def square_of_sum(n):
    """Returns the square of the sum of the first n natural numbers"""
    return int((n * (n + 1) / 2) ** 2)


def sum_of_squares(n):
    """Returns the sum of squares of the first n natural numbers"""
    return int(n * (n + 1) * (2 * n + 1) / 6)

def difference_of_squares(n):
    """Returns the difference between the square of the sum and the sum of squares of the first n natural numbers."""
    return square_of_sum(n) - sum_of_squares(n)

def square_of_sum(number):
    """Returns the square of the sum of the first 'number' natural numbers"""
    return (number*(number+1)//2)**2


def sum_of_squares(number):
    """Returns the sum of squares of the first 'number' natural numbers"""
    return ((number*number*(number+1)*(number+1))//6)


def difference_of_squares(number):
    """Returns the difference between the square of the sum and the sum of squares of the first 'number' natural numbers."""
    return abs(square_of_sum(number)-sum_of_squares(number))
