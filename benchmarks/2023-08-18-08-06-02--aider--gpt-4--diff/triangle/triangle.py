def equilateral(sides):
    if not _is_triangle(sides):
        return False
    return len(set(sides)) == 1


def isosceles(sides):
    if not _is_triangle(sides):
        return False
    return len(set(sides)) <= 2


def scalene(sides):
    if not _is_triangle(sides):
        return False
    return len(set(sides)) == 3


def _is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c
