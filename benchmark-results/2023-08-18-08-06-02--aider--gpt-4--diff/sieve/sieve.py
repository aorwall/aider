def primes(limit):
    if limit < 2:
        return []
    sieve = [False, False] + [True] * (limit - 1)
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            sieve[current*2::current] = [False] * len(sieve[current*2::current])
    return [num for num, prime in enumerate(sieve) if prime]
