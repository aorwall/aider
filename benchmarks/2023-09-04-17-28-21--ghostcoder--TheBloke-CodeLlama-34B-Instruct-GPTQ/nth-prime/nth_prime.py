import math

def prime(n):
    if n <= 0:
        raise ValueError("There is no zeroth prime")
    elif n == 1:
        return 2
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True