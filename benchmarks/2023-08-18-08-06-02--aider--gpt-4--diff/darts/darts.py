from math import sqrt

def score(x, y):
    distance = sqrt(x**2 + y**2)
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10
