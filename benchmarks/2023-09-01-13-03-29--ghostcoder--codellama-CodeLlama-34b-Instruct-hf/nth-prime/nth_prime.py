def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
