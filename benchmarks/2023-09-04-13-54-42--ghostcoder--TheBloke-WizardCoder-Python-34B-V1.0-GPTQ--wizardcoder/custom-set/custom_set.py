from typing import Any

class CustomSet:
    def __init__(self, elements=None):
        if not elements:
            self._elements = set()
        else:
            self._elements = set(elements)

    def isempty(self):
        return len(self._elements) == 0

    def __iter__(self):
        yield from self._elements

    def __contains__(self, element: Any) -> bool:
        return element in self._elements

    def issubset(self, other: 'CustomSet') -> bool:
        return all([elem in other for elem in self])

    def isdisjoint(self, other: 'CustomSet') -> bool:
        return not any([elem in other for elem in self])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CustomSet):
            raise TypeError('Can only compare two instances of CustomSet')
        return self._elements == other._elements

    def add(self, element: Any) -> None:
        self._elements.add(element)

    def intersection(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self._elements & other._elements)

    def __sub__(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self._elements - other._elements)

    def __add__(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self._elements | other._elements)
