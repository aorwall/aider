def factors(value):
    prime_factors = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            prime_factors.append(divisor)
            value = value / divisor
        else:
            divisor += 1

    return prime_factors