import math

def factors(value):
    factors = []
    divisor = 2
    while divisor <= math.sqrt(value):
        if value % divisor == 0:
            factors.append(divisor)
            value //= divisor
        else:
            divisor += 1
    if value > 1:
        factors.append(value)
    return factors
