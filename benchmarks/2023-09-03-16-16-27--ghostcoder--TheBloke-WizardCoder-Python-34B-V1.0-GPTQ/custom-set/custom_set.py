class CustomSet:
    def __init__(self, elements=None):
        self._elements = {}
        if elements is None:
            self._elements = {}
        else:
            for elem in elements:
                self.add(elem)


    def isempty(self):
        """Check if the set is empty"""
        return len(self._elements) == 0

    def __contains__(self, element):
        """Check if an element belongs to the set"""
        return element in self._elements

    def issubset(self, other):
        """Check if every element in this set is present in another set"""
        for elem in self._elements:
            if elem not in other:
                return False
        return True

    def isdisjoint(self, other):
        """Check if two sets have no common elements"""
        for elem in self._elements:
            if elem in other:
                return False
        return True

    def __eq__(self, other):
        """Check if two sets are equal"""
        if len(self._elements) != len(other._elements):
            return False
        for elem in self._elements:
            if elem not in other:
                return False
        return True

    def add(self, element):
        """Add an element to the set"""
        self._elements[element] = True

    def intersection(self, other):
        """Return a new set containing only the common elements between two sets"""
        res = CustomSet()
        for elem in self._elements:
            if elem in other:
                res.add(elem)
        return res

    def __sub__(self, other):
        """Subtract one set from another"""
        res = CustomSet()
        for elem in self._elements:
            if elem not in other:
                res.add(elem)
        return res

    def __add__(self, other):
        """Union of two sets"""
        res = CustomSet()
        for elem in self._elements:
            res.add(elem)
        for oth_elem in other._elements:
            res.add(oth_elem)
        return res

    def __iter__(self):
        """Iterate over the elements of the set"""
        return iter(list(self._elements))
