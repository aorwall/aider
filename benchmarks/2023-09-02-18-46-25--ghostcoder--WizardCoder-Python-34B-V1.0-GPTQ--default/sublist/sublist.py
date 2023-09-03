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
    Determine if list A is equal to, a superlist of, or a sublist of B, or none of the above.
    
    Args:
        list_one (list): List one for comparison.
        list_two (list): List two for comparison.
        
    Returns:
        str: One of SUBLIST, SUPERLIST, EQUAL, or UNEQUAL depending on the relationship between list_one and list_two.
    """

    # Check if lists are equal
    if list_one == list_two:
        return EQUAL

    # Check if list_one contains list_two
    if all([elem in list_one for elem in list_two]):
        return SUPERLIST

    # Check if list_two contains list_one
    if all([elem in list_two for elem in list_one]):
        return SUBLIST

    # If neither condition is met, they are unequal
    return UNEQUAL
