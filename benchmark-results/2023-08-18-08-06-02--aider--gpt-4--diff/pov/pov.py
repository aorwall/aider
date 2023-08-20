from json import dumps


class Tree:
    def __init__(self, label, children=None, parent=None):
        self.label = label
        self.children = children if children is not None else []
        self.parent = parent

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        if self.label == from_node:
            return self
        for child in self.children:
            try:
                new_root = child.from_pov(from_node)
            except ValueError:
                continue
            else:
                self.children.remove(child)
                child.children.append(self)
                self.parent = child
                return new_root
        raise ValueError("Tree could not be reoriented")

    def path_to(self, from_node, to_node):
        start_node = self.find(from_node)
        if start_node is None:
            raise ValueError("No path found")
        return start_node._path_to(to_node)

    def _path_to(self, to_node):
        if self.label == to_node:
            return [self.label]
        for child in self.children:
            try:
                path = child._path_to(to_node)
            except ValueError:
                continue
            else:
                return [self.label] + path
        if self.parent is not None:
            try:
                path = self.parent._path_to(to_node)
            except ValueError:
                return
            else:
                return [self.label] + path
        raise ValueError("No path found")
