import math

def score(x, y):
    distance_from_center = math.sqrt(x**2 + y**2)
    if distance_from_center > 10:
        return 0
    elif distance_from_center > 5: 
        return 1
    elif distance_from_center > 1:
        return 5
    else:
        return 10
