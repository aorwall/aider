def prime(n):
    if n < 1:
        raise ValueError('there is no zeroth prime')

    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1

    return primes[-1]
