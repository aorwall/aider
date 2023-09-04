def primes(limit):
    # Create a boolean array 'is_prime' of size limit+1 and initialize all elements to True
    is_prime = [True]*(limit+1)

    # Iterate from 2 to sqrt(limit)
    for p in range(2, int(limit**0.5)+1):
        # If is_prime[p] is True then it is a prime number
        if is_prime[p]:
            # Update all multiples of p to False
            for i in range(p*p, limit+1, p):
                is_prime[i] = False

    # Print all prime numbers greater than 1
    return [p for p in range(2, limit+1) if is_prime[p]]
