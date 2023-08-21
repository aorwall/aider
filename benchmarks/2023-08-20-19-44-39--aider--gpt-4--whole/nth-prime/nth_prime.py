def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    count = 0
    num = 1
    while count < number:
        num += 1
        if is_prime(num):
            count += 1
    return num
