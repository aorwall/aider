def equilateral(sides):
    if len(sides) != 3:
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if len(sides) != 3:
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides):
    if len(sides) != 3:
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]
