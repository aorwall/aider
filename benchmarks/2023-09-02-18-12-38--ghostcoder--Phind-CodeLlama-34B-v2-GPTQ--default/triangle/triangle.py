def equilateral(sides):
    return len(set(sides)) == 1 and all(side > 0 for side in sides)


def isosceles(sides):
    unique_sides = set(sides)
    return len(unique_sides) <= 2 and all(side > 0 for side in sides)


def scalene(sides):
    return len(set(sides)) >= 3 and all(side > 0 for side in sides)
