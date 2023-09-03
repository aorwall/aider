def equilateral(sides):
    """Check if a triangle is equilateral."""
    # Check if all sides are equal
    return len(set(sides)) == 1


def isosceles(sides):
    """Check if a triangle is is isosceles."""
    # Check if there are less than 3 unique sides (not valid)
    if len(set(sides)) < 3:
        return False
    # Check if there are more than 2 unique sides (scalene)
    elif len(set(sides)) > 2:
        return False
    else:
        # There are 2 unique sides (isosceles)
        return True

def scalene(sides):
    """Check if a triangle is scalene."""
    # Check if there are less than 3 unique sides (not valid)
    if len(set(sides)) < 3:
        return False
    # Check if there are more than 2 unique sides (scalene)
    elif len(set(sides)) > 2:
        return True
    else:
        # There are 2 unique sides (isosceles)
        return False
