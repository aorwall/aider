from json import dumps

class TreeNode:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def __repr__(self):
        return f"Tree({self.label}, {self.children})"

    def __hash__(self):
        return hash(self.label)

def Tree(*args, **kwargs):
    return TreeNode(*args, **kwargs)

def from_pov(tree, start_node):
    """Return a new tree rooted at the given node."""
    if start_node not in tree.nodes():
        raise ValueError("Node not found in tree.")

    # create a dictionary of nodes as keys and their parent nodes as values
    parents = {}
    for node in tree.nodes():
        for child in node.children:
            parents[child] = node

    # find all ancestors of the start node
    current_node = start_node
    ancestor_nodes = set([current_node])
    while current_node in parents:
        current_node = parents[current_node]
        ancestor_nodes.add(current_node)

    # create a new tree with the start node as the root
    new_tree = Tree(start_node.label)

    # add each child of the start node to the new tree
    for child in start_node.children:
        if child not in ancestor_nodes:
            new_tree.children.append(_reorient(child, start_node, ancestor_nodes))

    return new_tree

def _reorient(node, start_node, ancestor_nodes):
    """Recursively reparent the children of each node that is not an ancestor of the start node."""
    new_node = Tree(node.label)
    for child in node.children:
        if child not in ancestor_nodes:
            new_node.children.append(_reorient(child, start_node, ancestor_nodes))
    return new_node

def path_to(tree, from_node, to_node):
    """Returns the path between two nodes in the tree."""
    if from_node == to_node:
        return [from_node]

    # check if both nodes are present in the tree
    if from_node not in tree.nodes() or to_node not in tree.nodes():
        raise ValueError("Node not found in tree.")

    # create a dictionary of nodes as keys and their parent nodes as values
    parents = {}
    for node in tree.nodes():
        for child in node.children:
            parents[child] = node

    # find all ancestors of the end node
    current_node = to_node
    target_ancestors = set([current_node])
    while current_node in parents:
        current_node = parents[current_node]
        target_ancestors.add(current_node)

    # traverse upwards from the start node until we reach a common ancestor with the end node
    path = []
    current_node = from_node
    while current_node not in target_ancestors:
        path.append(current_node)
        if current_node not in parents:
            raise ValueError("No path found")
        current_node = parents[current_node]

    # add the path from the common ancestor to the end node
    path += [current_node, to_node]
    return list(reversed(path))

def nodes(tree):
    """Returns an iterable of all nodes in the tree."""
    yield tree
    for child in tree.children:
        yield from child.nodes()


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
        """Return a new tree rooted at the given node."""
        if from_node not in self.nodes():
            raise ValueError("Node not found in tree.")

        # create a dictionary of nodes as keys and their parent nodes as values
        parents = {}
        for node in self.nodes():
            for child in node.children:
                parents[child] = node

        # find all ancestors of the start node
        current_node = from_node
        ancestor_nodes = set([current_node])
        while current_node in parents:
            current_node = parents[current_node]
            ancestor_nodes.add(current_node)

        # create a new tree with the start node as the root
        new_tree = Tree(from_node.label)

        # add each child of the start node to the new tree
        for child in from_node.children:
            new_tree.children.append(self._reorient(child, from_node, ancestor_nodes))

        return new_tree

    def _reorient(self, node, start_node, ancestor_nodes):
        """Recursively reparent the children of each node that is not an ancestor of the start node."""
        new_node = Tree(node.label)
        for child in node.children:
            if child not in ancestor_nodes:
                new_node.children.append(self._reorient(child, start_node, ancestor_nodes))
        return new_node

    def path_to(self, from_node, to_node):
        """Returns the path between two nodes in the tree."""
        if from_node == to_node:
            return [from_node]

        # check if both nodes are present in the tree
        if from_node not in self.nodes() or to_node not in self.nodes():
            raise ValueError("Node not found in tree.")

        # create a dictionary of nodes as keys and their parent nodes as values
        parents = {}
        for node in self.nodes():
            for child in node.children:
                parents[child] = node

        # find all ancestors of the end node
        current_node = to_node
        target_ancestors = set([current_node])
        while current_node in parents:
            current_node = parents[current_node]
            target_ancestors.add(current_node)

        # traverse upwards from the start node until we reach a common ancestor with the end node
        path = []
        current_node = from_node
        while current_node not in target_ancestors:
            path.append(current_node)
            if current_node not in parents:
                raise ValueError("No path found")
            current_node = parents[current_node]

        # add the path from the common ancestor to the end node
        path += [current_node, to_node]
        return list(reversed(path))

    def nodes(self):
        """Returns an iterable of all nodes in the tree."""
        yield self
        for child in self.children:
            yield from child.nodes()
