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
        for element in self.elements:
            if element not in other.elements:
                return False
        return True

    def isdisjoint(self, other):
        for element in other.elements:
            if element in self.elements:
                return False
        return True

    def __eq__(self, other):
        if len(self.elements) != len(other.elements):
            return False
        for element in other.elements:
            if element not in self.elements:
                return False
        return True

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        new_set = CustomSet()
        for element in other.elements:
            if element in self.elements:
                new_set.add(element)
        return new_set

    def __sub__(self, other):
        new_set = CustomSet()
        for element in self.elements:
            if element not in other.elements:
                new_set.add(element)
        return new_set

    def __add__(self, other):
        new_set = CustomSet(self.elements)
        for element in other.elements:
            new_set.add(element)
        return new_set
