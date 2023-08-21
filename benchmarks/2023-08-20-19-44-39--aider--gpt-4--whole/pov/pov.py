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
        path = self.path_to(self.label, from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")
        for node in reversed(path):
            self.reparent(node)
        return self

    def path_to(self, from_node, to_node):
        if from_node == to_node:
            return [from_node]
        for child in self.children:
            path = child.path_to(from_node, to_node)
            if path:
                return [self.label] + path
        for child in self.children:
            for grandchild in child.children:
                path = grandchild.path_to(from_node, to_node)
                if path:
                    return [self.label, child.label] + path
        return None

    def reparent(self, new_root):
        if self.label == new_root:
            return
        for child in self.children:
            if child.label == new_root:
                self.children.remove(child)
                child.children.append(self)
                self.label, child.label = child.label, self.label
                self.children, child.children = child.children, self.children
                return
            child.reparent(new_root)
