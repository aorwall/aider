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
        if from_node not in self.__dict__():
            raise ValueError("Tree could not be reoriented")
        new_tree = self.__dict__()[from_node]
        return Tree(from_node, new_tree)

    def path_to(self, from_node, to_node):
        if from_node not in self.__dict__() or to_node not in self.__dict__():
            raise ValueError("No path found")
        path = []
        current_node = from_node
        while current_node != to_node:
            path.append(current_node)
            for child in self.__dict__()[current_node]:
                if to_node in child:
                    path.append(to_node)
                    return path
                else:
                    current_node = child
        return path