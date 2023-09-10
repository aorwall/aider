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
        if from_node not in self.children:
            raise ValueError("Tree could not be reoriented")

        new_tree = Tree(from_node)
        new_tree.children = [c.from_pov(from_node) for c in self.children]
        return new_tree

    def path_to(self, from_node, to_node):
        if from_node not in self.children:
            raise ValueError("No path found")

        if to_node not in self.children:
            raise ValueError("No path found")

        path = [from_node]
        while path[-1] != to_node:
            path.append(path[-1].parent)

        return path
