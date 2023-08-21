import re

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
    if not input_string:
        raise ValueError("tree missing")

    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("properties without delimiter")

    input_string = input_string[1:-1]  # remove the outermost parentheses

    nodes = re.split(r'\(|\)', input_string)  # split the string into nodes
    nodes = [node for node in nodes if node]  # remove empty nodes

    if not nodes:
        raise ValueError("tree with no nodes")

    root = None
    stack = []

    for node in nodes:
        properties = {}
        for prop in re.findall(r'([A-Z]+)\[([^\]]*)\]', node):
            key, value = prop
            if key.islower():
                raise ValueError("properties should be uppercase")
            value = value.replace("\\\\", "\\")
            value = value.replace("\\]", "]")
            value = value.replace("\\n", "")
            value = value.replace("\\t", " ")
            value = value.replace("\\n", "n")
            value = value.replace("\\t", "t")
            if key not in properties:
                properties[key] = []
            properties[key].append(value)

        tree = SgfTree(properties)

        if not root:
            root = tree
        else:
            stack[-1].children.append(tree)

        stack.append(tree)

    return root
