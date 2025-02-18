def primes(limit):
    primes = [False] * (limit + 1) # Fix Index Error by increasing array size by one
    primes[2:] = [True] * (limit - 2) # Set primes except 0 and 1

    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num*num, limit, num):
                primes[multiple] = False

    return [i for i, val in enumerate(primes) if val is True]
