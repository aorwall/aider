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
    # Check that the string starts and ends with the correct delimiters
    if not (input_string.startswith("(") and input_string.endswith(")")):
        raise ValueError("tree missing")

    # Remove the tree delimiters
    input_string = input_string[1:-1]

    # Split the nodes of the tree
    nodes = input_string.split(";")

    # If there are no nodes, raise an error
    if not nodes:
        raise ValueError("tree with no nodes")

    # Parse each node recursively
    root = _parse_node(nodes.pop(0))

    # Attach all children to the root
    while nodes:
        root.children.append(_parse_node(nodes.pop(0)))

    return SgfTree(root=root)

def _parse_node(node_string):
    properties = {}
    children = []

    # Split the properties by their delimiters
    property_strings = node_string.split("][")

    for property_string in property_strings:
        # Check that the property has a delimiter
        if "[" not in property_string or "]" not in property_string:
            raise ValueError("property without delimiter")

        # Get the key and value from the property string
        key, *value = property_string.split("[", 1)
        value = "[".join(value).rstrip("]")

        # Check that the key is uppercase
        if not key.isupper():
            raise ValueError("property must be in uppercase")

        # Add the property to the dictionary
        properties[key] = value

    return SgfTree(properties=properties, children=children)
