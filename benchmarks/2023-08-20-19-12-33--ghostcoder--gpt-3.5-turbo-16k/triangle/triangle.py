def equilateral(sides):
    if len(set(sides)) == 1 and all(side > 0 for side in sides):
        return True
    else:
        return False


def isosceles(sides):
    if len(set(sides)) <= 2 and all(side > 0 for side in sides):
        return True
    else:
        return False


def scalene(sides):
    if len(set(sides)) == 3 and all(side > 0 for side in sides):
        return True
    else:
        return False
