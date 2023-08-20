def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum_of_factors = sum(i for i in range(1, number) if number % i == 0)
    if sum_of_factors == number:
        return "perfect"
    elif sum_of_factors > number:
        return "abundant"
    else:
        return "deficient"