def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
