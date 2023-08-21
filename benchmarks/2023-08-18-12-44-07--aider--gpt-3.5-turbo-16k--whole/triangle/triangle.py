def equilateral(sides):
    a, b, c = sides
    if a == b == c and a != 0:
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sides
    if (a == b or b == c or a == c) and a + b >= c and b + c >= a and a + c >= b and a != 0:
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sides
    if a != b and b != c and a != c and a + b >= c and b + c >= a and a + c >= b and a != 0:
        return True
    else:
        return False
