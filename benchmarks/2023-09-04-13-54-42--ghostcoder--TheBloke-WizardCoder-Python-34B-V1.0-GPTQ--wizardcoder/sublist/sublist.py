"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import Union

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two) -> Union[str, bool]:
    """
    Determine the relationship between two lists.
    
    Args:
    - list_one (list): A list of integers.
    - list_two (list): Another list of integers.
    
    Returns:
    One of four possible strings:
    - "sublist": If list_one is a sublist of list_two.
    - "superlist": If list_one is a superlist of list_two.
    - "equal": If list_one and list_two are equivalent.
    - "unequal": If neither condition above applies.
    """
    # Check for equality first
    if len(list_one) != len(list_two):
        result = False
    else:
        result = all([x == y for x, y in zip(list_one, list_two)])

    if result:
        return EQUAL

    # Check for subset
    for i in range(len(list_one)):
        if list_one[i:] == list_two[:len(list_one)-i]:
            return SUBLIST

    # Check for superset
    for i in range(len(list_two)):
        if list_one[:len(list_two)-i] == list_two[i:]:
            return SUPERLIST

    return UNEQUAL


def sublist(list_one, list_two):
    pass
