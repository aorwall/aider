class CustomSet:
    def __init__(self, elements=None):
        # Initialize an empty set if no elements provided, otherwise convert list to set
        self._elements = set() if elements is None else set(elements)

    def isempty(self):
        return len(self._elements) == 0

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        # Check whether every item in this set exists in 'other' set
        return self._elements.issubset(other._elements)

    def isdisjoint(self, other):
        # Check whether two sets have no items in common
        return self._elements.isdisjoint(other._elements)

    def __eq__(self, other):
        # Check whether two sets are equal (same items)
        return self._elements == other._elements

    def add(self, element):
        # Add an element to the set
        self._elements.add(element)

    def intersection(self, other):
        # Return a new set with items found in both sets
        return CustomSet(self._elements & other._elements)

    def __sub__(self, other):
        # Return a new set with items from this set not found in other set
        return CustomSet(self._elements - other._elements)

    def __add__(self, other):
        # Return a new set with items from both sets
        return CustomSet(self._elements | other._elements)
