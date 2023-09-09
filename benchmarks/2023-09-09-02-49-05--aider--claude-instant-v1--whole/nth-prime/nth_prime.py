import math

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def prime(number):
    if number < 1:
        raise ValueError('Number must be greater than or equal to 1')
        
    for i in range(2,number+1):
        if is_prime(i):
            number -= 1
            if number == 0:
                return i
    raise ValueError('Number is greater than largest prime tested')
