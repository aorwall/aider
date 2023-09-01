def equilateral(sides):
    if len(sides) != 3:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    if len(sides) != 3:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2]:
        return True
    return False


def scalene(sides):
    if len(sides) != 3:
        return False
    if sides[0] != sides[1] and sides[1] != sides[2]:
        return True
    return False
