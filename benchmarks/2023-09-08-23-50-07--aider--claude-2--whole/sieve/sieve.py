def primes(limit):
    numbers = list(range(2, limit+1))
    for i in range(0, len(numbers)):
        prime = numbers[i]
        if prime != 0:
            for j in range(i+1, len(numbers)):
                if numbers[j] % prime == 0:
                    numbers[j] = 0
    return [x for x in numbers if x != 0]
