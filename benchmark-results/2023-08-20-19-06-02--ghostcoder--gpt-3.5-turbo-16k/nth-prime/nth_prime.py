def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes = []
    i = 2
    while len(primes) < number:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes[-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True