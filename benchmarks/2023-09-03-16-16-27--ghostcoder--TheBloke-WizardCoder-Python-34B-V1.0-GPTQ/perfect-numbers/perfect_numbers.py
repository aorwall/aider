def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Raise a value error if the input is not a positive integer greater than zero
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")
    aliquot_sum = sum([i for i in range(1, number//2 + 1) if number % i == 0])
    if aliquot_sum < number:
        return 'deficient'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'perfect'
