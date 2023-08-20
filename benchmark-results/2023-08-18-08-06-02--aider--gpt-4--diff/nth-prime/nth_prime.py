def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = []
    current = 2

    while len(primes) < number:
        if all(current % prime != 0 for prime in primes):
            primes.append(current)
        current += 1

    return primes[-1]
