class CustomSet:
    def __init__(self, elements=[]):
        self.elements = []
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(element in other.elements for element in self.elements)

    def isdisjoint(self, other):
        return not any(element in other.elements for element in self.elements)

    def __eq__(self, other):
        return set(self.elements) == set(other.elements)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        return CustomSet(element for element in self.elements if element in other.elements)

    def __sub__(self, other):
        return CustomSet(element for element in self.elements if element not in other.elements)

    def __add__(self, other):
        return CustomSet(self.elements + other.elements)
