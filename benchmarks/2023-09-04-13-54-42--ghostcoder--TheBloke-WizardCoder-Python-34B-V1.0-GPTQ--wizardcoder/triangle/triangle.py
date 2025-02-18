def equilateral(sides):
    a, b, c = sorted(sides)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sorted(sides)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sorted(sides)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a != b != c != a
