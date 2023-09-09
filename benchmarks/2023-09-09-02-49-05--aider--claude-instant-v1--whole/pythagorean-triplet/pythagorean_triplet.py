import math

def triplets_with_sum(number):
    triplets = []
    
    for a in range(1, number):
        for b in range(a+1, number):
            c = number - a - b
            c_squared = a**2 + b**2
            if c_squared == math.pow(c, 2):
                if a < b < c:
                    triplets.append([a, b, c])
                    
    return triplets
