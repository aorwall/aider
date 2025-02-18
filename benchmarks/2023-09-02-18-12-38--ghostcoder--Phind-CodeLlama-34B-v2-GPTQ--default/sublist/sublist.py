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
    if sorted(list_one) == sorted(list_two):
        return EQUAL
    elif len(list_one) > len(list_two) and all(i in list_one for i in sorted(list_two)):
        return SUPERLIST
    elif len(list_one) < len(list_two) and all(i in list_two for i in sorted(list_one)):
        return SUBLIST
    else:
        return UNEQUAL
