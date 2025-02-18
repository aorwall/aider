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
        """
        Reparent a tree on a selected node.

        Args:
            from_node (str): The label of the node to reparent the tree on.

        Returns:
            Tree: A new tree with the selected node as the root.
        """
        # Find the node to reparent the tree on
        node = self.find_node(from_node)

        # If the node is not found, raise an error
        if node is None:
            raise ValueError("Node not found")

        # Create a new tree with the selected node as the root
        new_tree = Tree(node.label)

        # Add the children of the selected node to the new tree
        for child in node.children:
            new_tree.children.append(child)

        # Return the new tree
        return new_tree

    def path_to(self, from_node, to_node):
        """
        Find the path between two nodes in a tree.

        Args:
            from_node (str): The label of the starting node.
            to_node (str): The label of the ending node.

        Returns:
            list: A list of nodes in the path between the starting and ending nodes.
        """
        # Find the starting and ending nodes
        start_node = self.find_node(from_node)
        end_node = self.find_node(to_node)

        # If either node is not found, raise an error
        if start_node is None or end_node is None:
            raise ValueError("Node not found")

        # Create a list to store the path
        path = []

        # Add the starting node to the path
        path.append(start_node)

        # While the current node is not the ending node, add its children to the path
        while path[-1] != end_node:
            for child in path[-1].children:
                path.append(child)

        # Return the path
        return path

    def find_node(self, label):
        """
        Find a node in a tree by its label.

        Args:
            label (str): The label of the node to find.

        Returns:
            Tree: The node with the given label, or None if it is not found.
        """
        # If the current node has the given label, return it
        if self.label == label:
            return self

        # If the current node has children, search them for the given label
        for child in self.children:
            found_node = child.find_node(label)
            if found_node is not None:
                return found_node

        # If the node is not found, return None
        return None