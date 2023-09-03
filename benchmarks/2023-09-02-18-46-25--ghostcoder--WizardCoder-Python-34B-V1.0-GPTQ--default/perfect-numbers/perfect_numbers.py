def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    def aliquot_sum():
        return sum([i for i in range(1, number//2 + 1) if number % i == 0])

    if aliquot_sum() == number:
        return "perfect"
    elif aliquot_sum() > number:
        return "abundant"
    else:
        return "deficient"
