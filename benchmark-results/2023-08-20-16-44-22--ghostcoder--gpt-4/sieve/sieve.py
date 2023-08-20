def primes(limit):
    sieve = [True] * (limit + 1)
    for x in range(2, int(limit**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, limit + 1, x):
                sieve[i] = False
    return [p for p in range(2, limit + 1) if sieve[p]]