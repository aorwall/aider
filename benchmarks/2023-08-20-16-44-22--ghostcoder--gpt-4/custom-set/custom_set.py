class CustomSet:
    def __init__(self, elements=[]):
        self.set = set(elements)

    def isempty(self):
        return len(self.set) == 0

    def __contains__(self, element):
        return element in self.set

    def issubset(self, other):
        return self.set.issubset(other.set)

    def isdisjoint(self, other):
        return self.set.isdisjoint(other.set)

    def __eq__(self, other):
        return self.set == other.set

    def add(self, element):
        self.set.add(element)

    def intersection(self, other):
        return CustomSet(self.set.intersection(other.set))

    def __sub__(self, other):
        return CustomSet(self.set - other.set)

    def __add__(self, other):
        return CustomSet(self.set.union(other.set))