def classify(number):
    """A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    aliquot_sum = 0
    for factor in range(1, number):
        if number % factor == 0:
            aliquot_sum += factor
            
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
