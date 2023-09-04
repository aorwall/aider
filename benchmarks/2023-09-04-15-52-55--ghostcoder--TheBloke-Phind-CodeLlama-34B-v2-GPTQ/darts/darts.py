import math

def score(x, y):
    r = math.sqrt(x**2 + y**2)

    if r > 10:
        return 0
    elif r <= 10 and r >= 5:
        return 1
    elif r < 5 and r >= 1:
        return 5
    else: # r < 1
        return 10
