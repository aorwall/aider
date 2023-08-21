def factors(value):
    factors = []
    divisor = 2
    while value > 1:
        if value % divisor == 0:
            factors.append(divisor)
            value = value / divisor
        else:
            divisor += 1
    return factors
