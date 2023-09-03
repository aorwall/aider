def primes(limit):
    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    prime = [True for _ in range(limit + 1)]
    p = 2
    while (p * p <= limit):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Collect and return all prime numbers
    return [p for p in range(2, limit + 1) if prime[p]]
