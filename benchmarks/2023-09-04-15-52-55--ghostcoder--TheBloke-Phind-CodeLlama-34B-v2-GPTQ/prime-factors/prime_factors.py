def factors(num):
    # Initialize a list to hold the prime factors
    prime_factors = []

    # Check for divisibility by 2 until num becomes odd
    while num % 2 == 0:
        prime_factors.append(2)
        num = num / 2

    # Check for divisibility by odd numbers up to sqrt(num)
    for i in range(3, int(num**0.5)+1, 2):
        while num % i== 0:
            prime_factors.append(i)
            num = num / i

    # If num is greater than 2 (which means it was not divided evenly), then it's a prime factor
    if num > 2:
        prime_factors.append(int(num))

    return prime_factors