"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary, but unique value.
An integer is traditionally used because it’s memory efficient. It is a common 
practice to export both constants and functions that work with those constants (ex. 
the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories. Do not modify these values!
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
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):
    """
    Determines if one list is a sublist of another list.
    
    Args:
        list_one: A list of integers.
        list_two: Another list of integers.
    
    Returns:
        SUBLIST, SUPERLIST, EQUAL or UNEQUAL depending on whether list_one is a sublist,
            superlist, or equal to list_two respectively.
    """
    # Check if lists are equal
    if len(list_one) == len(list_two) and sorted(list_one) == sorted(list_two):
        return EQUAL

    # Check if list_one is a sublist of list_two
    elif all([elem in list_two for elem in list_one]):
        return SUBLIST

    # Check if list_one is a superlist of list_two
    elif all([elem in list_one for elem in list_two]):
        return SUPERLIST
    else:
        return UNEQUAL
