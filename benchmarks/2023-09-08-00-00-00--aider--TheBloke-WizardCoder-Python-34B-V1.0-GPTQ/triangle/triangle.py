def is_equilateral(sides):
    a, b, c = sorted(sides)
    return a == b == c

def is_isosceles(sides):
    a, b, c = sorted(sides)
    return a == b or b == c or a == c

def is_scalene(sides):
    a, b, c = sorted(sides)
    return a != b and b != c and a != c
