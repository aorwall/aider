def equilateral(sides):
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    a, b, c = sorted(sides)
    return (a <= b <= c) and ((a == b) or (b == c))


def scalene(sides):
    a, b, c = sides
    return a != b != c != a
