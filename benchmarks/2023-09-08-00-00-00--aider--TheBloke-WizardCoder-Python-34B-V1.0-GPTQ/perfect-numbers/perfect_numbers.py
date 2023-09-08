def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    def aliquot_sum(n):
        return sum(d for d in range(1, n) if n % d == 0)

    aliquot = aliquot_sum(number)

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
