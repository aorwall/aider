def primes(limit):
    if limit < 2:
        return []

    # Create a boolean array "is_prime[0..n]" and initialize all entries it as true.
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    # Start with the first prime number, 2.
    p = 2
    while p*p <= limit:
        # If is_prime[p] is True, then mark all its multiples as False.
        if is_prime[p]:
            for i in range(p*p, limit+1, p):
                is_prime[i] = False
        p += 1

    # Return a list of prime numbers.
    return [x for x in range(2, limit+1) if is_prime[x]]
