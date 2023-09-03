def prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
