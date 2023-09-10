class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return self.elements.issubset(other)

    def isdisjoint(self, other):
        return self.elements.isdisjoint(other)

    def __eq__(self, other):
        return self.elements == other

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        return self.elements.intersection(other)

    def __sub__(self, other):
        return self.elements.difference(other)

    def __add__(self, other):
        return self.elements.union(other)
