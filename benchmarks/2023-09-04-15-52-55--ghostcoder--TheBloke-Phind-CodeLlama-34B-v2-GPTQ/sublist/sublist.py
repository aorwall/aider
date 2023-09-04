"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 0
UNEQUAL = 2

def sublist(list_one, list_two):
    """
    This function checks whether one list is a sublist, superlist, equal or unequal to another list.
    
    Args:
      list_one: First list to compare
      list_two: Second list to compare
      
    Returns:
      One of the enumerated constants indicating the relationship between the two lists.
    """
    if not list_one or not list_two:
        # Both lists must be nonempty for them to have a meaningful relationship.
        raise ValueError("Both input lists must be nonempty")

    if set(list_one) == set(list_two):
        # The sets are equal only when the lists are equal.
        return EQUAL
    elif all(i in list_two for i in list_one):
        # All elements of list_one are in list_two => list_one is a sublist of list_two.
        return SUBLIST
    elif all(i in list_one for i in list_two):
        # All elements of list_two are in list_one => list_one is a superlist of list_two.
        return SUPERLIST
    else:
        # Neither list is a subset of the other and neither is equal to the other.
        return UNEQUAL
