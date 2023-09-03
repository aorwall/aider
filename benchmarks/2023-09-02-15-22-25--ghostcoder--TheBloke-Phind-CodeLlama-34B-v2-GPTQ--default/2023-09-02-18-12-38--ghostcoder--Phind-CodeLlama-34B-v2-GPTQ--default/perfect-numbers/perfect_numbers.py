def aliquot_sum(number):
    """ Calculate the sum of proper divisors of a given number.
    
    :param number: int a positive integer
    :return: int the sum of the proper divisors of the input number
    """
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum
def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum_result = aliquot_sum(number)
    if aliquot_sum_result == number:
        return "Perfect"
    elif aliquot_sum_result > number:
        return "Abundant"
    else:
        return "Deficient"
