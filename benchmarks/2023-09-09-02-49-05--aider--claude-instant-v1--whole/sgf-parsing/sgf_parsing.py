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


def parse_text(text):
    text = re.sub(r'\\(?!\n)', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def parse(input_string):
    if not input_string:
        raise ValueError("tree missing")

    current = None
    properties = {}
    children = []

    for char in input_string:
        if char == ';':
            if not properties:
                continue
            for key, value in properties.items():
                if not key.isupper():
                    raise ValueError("property must be in uppercase")
            current = SgfTree(properties, children)
            properties = {}
            children.append(current)
        elif char == '(':
            if not current:
                current = SgfTree(properties, children)
            else:
                raise ValueError("tree with no nodes")
        elif char == ')':
            return current
        elif char == ']':
            key, value = properties.get(key, []), value
            properties[key] = value + char
        else:
            key += char

    raise ValueError("input not fully parsed")

    return current
