def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate the sum of all positive divisors of 'number'.
    divisor_sum = sum([divisor for divisor in range(1, number // 2 + 1) if number % divisor == 0])

    if divisor_sum == number:
        return "perfect"
    elif divisor_sum > number:
        return "abundant"
    else:
        return "deficient"
