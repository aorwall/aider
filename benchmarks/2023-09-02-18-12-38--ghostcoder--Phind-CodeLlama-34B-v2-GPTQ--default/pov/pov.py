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
        try:
            root = self._find_node(from_node)
            if root is None:
                raise ValueError("Node not found")

            tree = Tree(root.label)
            for child in sorted(root.children):
                subtree = Tree(child.label)
                subtree.children = [Tree(c.label) for c in sorted(child.children)]
                tree.children.append(subtree)

            return tree
        except Exception as e:
            raise ValueError("Tree could not be reoriented") from e

    def path_to(self, from_node, to_node):
        try:
            start = self._find_node(from_node)
            end = self._find_node(to_node)
            if start is None or end is None:
                raise ValueError("Node not found")

            current = end
            path = []
            while current != start:
                path.append(current.label)
                current = current.parent
            path.reverse()
            return path + [start.label]
        except Exception as e:
            raise ValueError("No path found") from e

    def _find_node(self, label):
        stack = [self]
        while stack:
            node = stack.pop()
            if node.label == label:
                return node
            else:
                stack.extend(reversed(node.children))
        return None

    def path_to(self, from_node, to_node):
        try:
            # Your implementation here
            pass
        except Exception as e:
            raise ValueError("No path found") from e
