from collections import deque
from itertools import chain
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
        queue = deque([(None, self)])
        while queue:
            parent, current = queue.popleft()
            if current.label == from_node:
                return Tree(current.label, [Tree(parent.label, [child.__dict__() for child in parent.children]) for parent in queue])
            elif current.children:
                queue.extend((current, child) for child in current.children)
        raise ValueError("No such node")

    def path_to(self, from_node, to_node):
        try:
            tree = self.from_pov(from_node)
            queue = deque([(None, tree)])
            while queue:
                _, current = queue.popleft()
                if current.label == to_node:
                    return True
                elif current.children:
                    queue.extend((current, child) for child in current.children)
            return False
        except ValueError:
            raise ValueError("No such node")
