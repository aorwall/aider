def classify(number):
    """ Classify a positive integer as perfect, abundant, or deficient.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    factors_sum = sum([i for i in range(1, number) if number % i == 0])

    if factors_sum == number:
        return "perfect"
    elif factors_sum > number:
        return "abundant"
    else:
        return "deficient"
