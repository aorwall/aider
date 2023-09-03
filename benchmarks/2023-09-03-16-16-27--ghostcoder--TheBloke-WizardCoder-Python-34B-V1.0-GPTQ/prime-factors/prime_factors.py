def factors(value):
    """Return a list of prime factors of a given number."""
    primes = []
    while value % 2 == 0:
        primes.append(2)
        value //= 2

    # Check odd numbers starting from 3
    num = 3
    while value > 1:
        if value % num == 0:
            primes.append(num)
            value //= num
        else:
            num += 2

    return primes
