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
        if isinstance(other, str):
            return self.label == other
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        if from_node not in self.flatten():
            raise ValueError("Node not found in tree")
        
        def reorient(current_node, parent=None):
            current_node.children = [c for c in current_node.children if c.label != parent]
            return current_node
        
        return reorient(next(n for n in self.flatten() if n.label == from_node))

    def flatten(self):
        nodes = [self]
        for child in self.children:
            nodes.extend(child.flatten())
        return nodes
    
    def path_to(self, from_node, to_node):
        if from_node not in self.flatten() or to_node not in self.flatten():
            raise ValueError("Node not found in tree")
            
        current = next(n for n in self.flatten() if n.label == from_node)
        path = []
        while current and current.label != to_node:
            path.append(current.label)
            if not current.children:
                raise ValueError("No path found between nodes")
            current = current.children[0]
        if current.label == to_node:
            path.append(to_node)
            return path
        else:
            raise ValueError("No path found between nodes")
