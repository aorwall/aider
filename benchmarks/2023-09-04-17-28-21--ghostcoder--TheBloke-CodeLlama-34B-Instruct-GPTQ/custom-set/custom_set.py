from typing import Any

class CustomSet:
    def __init__(self, elements=None):
        # Initialize empty list to store elements
        self._elements = []

        # If elements argument is passed, add them to the set
        if elements is not None:
            for element in elements:
                self.add(element)

    def isempty(self) -> bool:
        """Return True if the set contains no elements."""
        return len(self._elements) == 0

    def __contains__(self, element: Any) -> bool:
        """Return True if the element is in the set."""
        return element in self._elements

    def issubset(self, other: "CustomSet") -> bool:
        """Return True if every element in the set is also in other."""
        return all(elem in other for elem in self._elements)

    def isdisjoint(self, other: "CustomSet") -> bool:
        """Return True if there are no common elements between the sets."""
        return not any(elem in other for elem in self._elements)

    def __eq__(self, other: object) -> bool:
        """Return True if the sets contain the same elements."""
        return self._elements == getattr(other, "_elements", [])

    def add(self, element: Any) -> None:
        """Add an element to the set."""
        if element not in self._elements:
            self._elements.append(element)

    def intersection(self, other: "CustomSet") -> "CustomSet":
        """Return a new set containing only the common elements."""
        return CustomSet([elem for elem in self._elements if elem in other])

    def __sub__(self, other: "CustomSet") -> "CustomSet":
        """Return a new set containing only the elements in the left operand but not in the right operand."""
        return CustomSet([elem for elem in self._elements if elem not in other])

    def __add__(self, other: "CustomSet") -> "CustomSet":
        """Return a new set containing all elements from both sets."""
        return CustomSet(self._elements + other._elements)
