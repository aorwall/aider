def equilateral(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 1


def isosceles(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) <= 2


def scalene(sides):
    if not is_triangle(sides):
        return False
    return len(set(sides)) == 3


def is_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b
