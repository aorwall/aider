def primes(limit):
    if limit < 2:
        return []
    else:
        primes_list = [True] * (limit + 1)
        primes_list[0] = primes_list[1] = False

        for i in range(2, int(limit ** 0.5) + 1):
            if primes_list[i]:
                for j in range(i * i, limit + 1, i):
                    primes_list[j] = False

        return [i for i, is_prime in enumerate(primes_list) if is_prime]