import math

def equilateral(sides):
  if len(set(sides)) == 1:
    return True
  else:
    return False

def isosceles(sides):
  if len(set(sides)) <= 2:
    return True
  else:  
    return False
  
def scalene(sides):
  if len(set(sides)) == 3:
    return True
  else:
    return False
