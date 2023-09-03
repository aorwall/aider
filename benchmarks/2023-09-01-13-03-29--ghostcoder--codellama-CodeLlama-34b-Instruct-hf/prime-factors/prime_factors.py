def factors(value):
    factors = []
    for i in range(2, int(value**0.5) + 1):
        while value % i == 0:
            factors.append(i)
            value //= i
    if value > 1:
        factors.append(value)
    return factors