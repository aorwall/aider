from math import sqrt

def classify(number):
    """Classify a positive integer as perfect, abundant or deficient based on Nicomachus' scheme.

    :param number: int
    :return: str
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    aliquot_sum = sum(list(filter(lambda x: number % x == 0 and x < number, range(1, int(number)))))
    
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
