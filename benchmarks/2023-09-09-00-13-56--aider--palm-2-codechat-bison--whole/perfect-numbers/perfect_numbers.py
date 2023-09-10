def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # calculate the aliquot sum of the input number
    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i

    # classify the input number based on its aliquot sum
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
