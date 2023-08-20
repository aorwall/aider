from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        path = self._path_to(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")
        return self._from_path(path)

    def path_to(self, from_node, to_node):
        tree = self.from_pov(from_node)
        path = tree._path_to(to_node)
        if not path:
            raise ValueError("No path found")
        return [node.label for node in path]

    def _path_to(self, label, path=None):
        if path is None:
            path = []
        if self.label == label:
            return path + [self]
        for child in self.children:
            result = child._path_to(label, path + [self])
            if result:
                return result
        return None

    def _from_path(self, path):
        if not path:
            return None
        node = path[-1]
        if node in self.children:
            self.children.remove(node)
            if path[:-1]:
                self.children.append(self._from_path(path[:-1]))
        return Tree(node.label, self.children)