def primes(limit):
    """
    Returns a list of prime numbers up to limit using the Sieve of Eratosthenes algorithm.
    """
    if limit < 2:
        return []

    # Create a boolean array "is_prime" indicating whether each number is prime or composite
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    # Collect all the prime numbers into a list
    primes = []
    for num in range(2, len(is_prime)):
        if is_prime[num]:
            primes.append(num)

    return primes
