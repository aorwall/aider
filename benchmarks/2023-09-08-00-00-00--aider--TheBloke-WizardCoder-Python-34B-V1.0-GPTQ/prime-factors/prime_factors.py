def factors(value):
    factors_list = []
    divisor = 2
    while divisor <= value:
        if value % divisor == 0:
            factors_list.append(divisor)
            value //= divisor
        else:
            divisor += 1
    return factors_list
