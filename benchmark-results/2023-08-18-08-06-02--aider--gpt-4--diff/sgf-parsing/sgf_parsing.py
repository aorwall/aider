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


import re

def parse(input_string):
    if not input_string or not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("tree missing")

    nodes = re.findall(r'\(;[^)]*\)', input_string)
    if not nodes:
        raise ValueError("tree with no nodes")

    def parse_node(node):
        properties = re.findall(r'([A-Z]+)\[((?:\\[\]])*[^\]]*)\]', node)

        property_dict = {}
        for key, value in properties:
            if not key.isupper():
                raise ValueError("property must be in uppercase")

            value = value.replace("\\\\", "\\").replace("\\]", "]")

            if key in property_dict:
                property_dict[key].append(value)
            else:
                property_dict[key] = [value]

        return SgfTree(property_dict, [])

    root = parse_node(nodes[0])
    for node in nodes[1:]:
        root.children.append(parse_node(node))

    return root
