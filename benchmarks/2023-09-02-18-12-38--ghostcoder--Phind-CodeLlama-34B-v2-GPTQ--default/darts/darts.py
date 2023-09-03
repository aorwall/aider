import math
def score(x, y):
    # Calculate the distance from the origin using Pythagorean theorem
    distance = math.sqrt(x**2 + y**2)

    # Determine the points scored based on the distance
    if distance <= 10:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 1:
        return 1
    else:
        return 0
