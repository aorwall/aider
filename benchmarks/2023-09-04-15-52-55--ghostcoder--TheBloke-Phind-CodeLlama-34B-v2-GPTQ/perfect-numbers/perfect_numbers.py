def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Check if the number is a positive integer
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate the aliquot sum
    aliquot_sum = sum([i for i in range(1, number) if number % i == 0])

    # Classify the number
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'
