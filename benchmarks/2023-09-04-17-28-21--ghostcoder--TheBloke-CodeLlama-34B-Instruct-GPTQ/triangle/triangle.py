def equilateral(sides):
    return len(set(sides)) == 1


def isosceles(sides):
    return len(set(sides)) <= 2


def scalene(sides):
    return len(set(sides)) == 3
