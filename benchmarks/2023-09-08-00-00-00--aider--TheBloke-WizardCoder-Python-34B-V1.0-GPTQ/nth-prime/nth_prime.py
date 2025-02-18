def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = []
    i = 2
    while len(primes) < number:
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1
    return primes[-1]
