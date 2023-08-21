def primes(limit):
    sieve = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if sieve[p]]
