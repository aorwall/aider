from collections import deque
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
        """Returns the subtree starting at the given node."""
        # Find the node in the tree
        queue = deque([self])
        while len(queue) > 0:
            current = queue.popleft()
            if current.label == from_node:
                break
            elif current.children != []:
                queue += current.children
        else:
            raise ValueError("Node not found.")

        # Return the subtree
        result = Tree(current.label)
        queue = deque([result])
        while len(queue) > 0:
            parent = queue.popleft()
            for child in current.children:
                new_child = Tree(child.label)
                parent.children.append(new_child)
                queue.append(new_child)
                current = child
        return result

    def path_to(self, from_node, to_node):
        """Returns the path between two nodes in the tree."""
        # Find the nodes in the tree
        queue = deque([self])
        while len(queue) > 0:
            current = queue.popleft()
            if current.label == from_node:
                from_node = current
            elif current.label == to_node:
                to_node = current
            elif current.children != []:
                queue += current.children
        else:
            raise ValueError("One or both nodes not found.")

        # Find the path between them
        path = []
        current = to_node
        while current != from_node:
            path.insert(0, current.label)
            current = current.parent
        return path
