import math

def triplets_with_sum(number):
    result = []
    for a in range(1, int((number / 3) - 1)):
        for b in range(int((math.sqrt(2 * number ** 2 - 2 * a ** 2)) // 2), number - a):
            c = number - a - b
            if a**2 + b**2 == c**2:
                result.append([a, b, c])
    return result
