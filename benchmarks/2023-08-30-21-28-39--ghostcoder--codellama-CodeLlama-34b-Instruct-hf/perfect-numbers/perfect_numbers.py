def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors == number:
        return "perfect"
    elif sum_of_divisors > number:
        return "abundant"
    else:
        return "deficient"
