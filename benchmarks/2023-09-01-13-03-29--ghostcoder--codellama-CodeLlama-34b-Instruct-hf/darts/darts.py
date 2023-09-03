def score(x, y):
    # Calculate the distance from the origin to the point (x, y)
    distance = (x ** 2 + y ** 2) ** 0.5

    # Determine the earned points based on the distance
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    else:
        return 10
