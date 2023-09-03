def prime(number):
    """Return the nth prime number."""

    # Check for invalid inputs
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes = []
    num = 2
    while len(primes) != number:
        for p in primes:
            if num % p == 0:
                break
        else:  # no factor found, so this is a prime
            primes.append(num)
        num += 1

    return primes[-1]
