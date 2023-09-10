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
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
  """
  Given any two lists `A` and `B`, determine if:

  - List `A` is equal to list `B`; or
  - List `A` contains list `B` (`A` is a superlist of `B`); or
  - List `A` is contained by list `B` (`A` is a sublist of `B`); or
  - None of the above is true, thus lists `A` and `B` are unequal

  Specifically, list `A` is equal to list `B` if both lists have the same values in the same order.
  List `A` is a superlist of `B` if `A` contains a sub-sequence of values equal to `B`.
  List `A` is a sublist of `B` if `B` contains a sub-sequence of values equal to `A`.

  Args:
    list_one: The first list to compare.
    list_two: The second list to compare.

  Returns:
    One of the following values:
    - SUBLIST: If `A` is a sublist of `B`.
    - SUPERLIST: If `A` is a superlist of `B`.
    - EQUAL: If `A` is equal to `B`.
    - UNEQUAL: If `A` is not equal to, a sublist of, or a superlist of `B`.
