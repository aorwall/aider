from math import sqrt

def factors(value):
    if value <= 1:
        raise ValueError("Value must be greater than 1")

    primes = []
    while value % 2 == 0:
        primes.append(2)
        value //= 2

    for i in range(3, int(sqrt(value)) + 1, 2):
        while value % i == 0:
            primes.append(i)
            value //= i

    if value > 2:
        primes.append(value)

    return primes
