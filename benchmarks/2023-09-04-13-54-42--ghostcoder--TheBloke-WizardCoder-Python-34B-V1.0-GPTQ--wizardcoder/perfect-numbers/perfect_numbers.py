def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Raise a ValueError if the input is not a positive integer.
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate the aliquot sum of the input number.
    aliquot_sum = sum([i for i in range(1, number // 2 + 1) if number % i == 0])

    # Determine the classification of the input number based on its aliquot sum.
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'
