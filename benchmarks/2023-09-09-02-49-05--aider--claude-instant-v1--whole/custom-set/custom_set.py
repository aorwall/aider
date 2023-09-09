from typing import Set

class CustomSet:
    def __init__(self, elements: Set = None):
        if elements is None:
            elements = set()
        self.elements = elements

    def isempty(self) -> bool:
        return len(self.elements) == 0

    def __contains__(self, element) -> bool:
        return element in self.elements

    def issubset(self, other: 'CustomSet') -> bool:
        return all(item in other.elements for item in self.elements)

    def isdisjoint(self, other: 'CustomSet') -> bool:
        return len(self.elements & other.elements) == 0

    def __eq__(self, other: 'CustomSet') -> bool:
        return self.elements == other.elements

    def add(self, element) -> None:
        self.elements.add(element)

    def intersection(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self.elements & other.elements) 

    def __sub__(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self.elements - other.elements)

    def __add__(self, other: 'CustomSet') -> 'CustomSet':
        return CustomSet(self.elements | other.elements)
