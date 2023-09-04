def primes(limit):
    if limit < 2:
        return []

    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will finally
    # be false if i is Not a prime, else true.
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    # Iterate over all prime numbers less than or equal to sqrt(limit)
    for p in range(2, int(limit**0.5) + 1):

        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:

            # Update all multiples of p greater than or equal to the square of it
            # numbers which are multiple of p and are less than p^2 are already been marked.
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    # Return a list of prime numbers
    return [x for x in range(2, limit + 1) if is_prime[x]]
