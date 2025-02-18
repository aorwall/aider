class CustomSet:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = set()
        else:
            self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        if isinstance(other, self.__class__):
            return self.elements.issubset(other.elements)
        else:
            return self.elements.issubset(other)

    def isdisjoint(self, other):
        if isinstance(other, self.__class__):
            return self.elements.isdisjoint(other.elements)
        else:
            return self.elements.isdisjoint(other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.elements == other.elements
        else:
            return False

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        if isinstance(other, self.__class__):
            return CustomSet(self.elements.intersection(other.elements))
        else:
            return CustomSet(self.elements.intersection(other))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return CustomSet(self.elements - other.elements)
        else:
            return CustomSet(self.elements - other)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return CustomSet(self.elements | other.elements)
        else:
            return CustomSet(self.elements | set(other))
