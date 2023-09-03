def equilateral(sides):
    """Determines if a triangle with given sides is an equilateral triangle."""
    return len(set(sides)) == 1 and all(side > 0 for side in sides)


def isosceles(sides):
    """Determines if a triangle with given sides is an isosceles triangle."""
    unique_sides = set(sides)
    return len(unique_sides) < 3 or max(unique_sides) >= min(sides) - max(sides)


def scalene(sides):
    """Determines if a triangle with given sides is a scalene triangle."""
    return len(set(sides)) == 3 and all(side > 0 for side in sides)
