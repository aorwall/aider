class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    # Split the input string into a list of tokens.
    tokens = input_string.split(";")

    # Create an empty tree.
    tree = SgfTree()

    # Iterate over the tokens.
    for token in tokens:
        # If the token is a property, add it to the current node.
        if token.startswith("[") and token.endswith("]"):
            key, value = token[1:-1].split("=")
            tree.properties[key.upper()] = value

        # If the token is a node, create a new node and add it to the current node's children.
        elif token.startswith("(") and token.endswith(")"):
            new_node = SgfTree()
            tree.children.append(new_node)
            parse(token[1:-1])

    # Return the tree.
    return tree
