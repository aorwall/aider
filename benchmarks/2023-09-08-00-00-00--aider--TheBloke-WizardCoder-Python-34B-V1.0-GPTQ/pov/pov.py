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
        if from_node not in self.label:
            raise ValueError("No path found")

        def traverse(node, target):
            if node.label == target:
                return node
            for child in node.children:
                result = traverse(child, target)
                if result:
                    return result
            return None

        new_root = traverse(self, from_node)
        if not new_root:
            raise ValueError("Tree could not be reoriented")

        def reconstruct(node):
            new_node = Tree(node.label)
            for child in node.children:
                if child.label != from_node:
                    new_child = reorient(child)
                    new_node.children.append(new_child)
            return new_node

        return reconstruct(new_root)

    def path_to(self, from_node, to_node):
        if from_node not in self.label or to_node not in self.label:
            raise ValueError("No path found")

        def traverse(node, target, path):
            path.append(node.label)
            if node.label == target:
                return path
            for child in node.children:
                result = traverse(child, target, path)
                if result:
                    return result
            path.pop()
            return None

        path = traverse(self, to_node, [from_node])
        if not path:
            raise ValueError("No path found")

        return path
