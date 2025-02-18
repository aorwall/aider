from typing import List, Union

class CustomSet:
    def __init__(self, elements: Union[List[int], set]=None):
        if elements is None:
            self._elements = set()
        elif type(elements) is set:
            self._elements = elements
        else:
            self._elements = set(elements)

    def isempty(self) -> bool:
        return len(self._elements) == 0

    def __contains__(self, element: int) -> bool:
        return element in self._elements

    def issubset(self, other: 'CustomSet') -> bool:
        return all([item in other for item in self._elements])

    def isdisjoint(self, other: 'CustomSet') -> bool:
        return not bool(self._elements.intersection(other._elements))

    def __eq__(self, other: 'CustomSet') -> bool:
        return self._elements == other._elements

    def add(self, element: int):
        if element not in self._elements:
            self._elements.add(element)

    def intersection(self, other: 'CustomSet'):
        return self._elements.intersection(other._elements)

    def __sub__(self, other: 'CustomSet'):
        return self._elements - other._elements

    def __add__(self, other: 'CustomSet'):
        new_set = self._elements.copy()
        new_set.update(other._elements)
        return new_set
