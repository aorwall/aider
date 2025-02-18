import re
from collections import defaultdict

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
    tree = _parse_node(input_string)
    if input_string[-1] != ')':
        raise ValueError("Invalid SGF: Missing closing parenthesis")
    return tree

def _parse_node(input_string):
    node = SgfTree()
    rest = input_string.strip()
    while rest and rest[0] != ';':
        prop_ident, rest = _parse_prop_ident(rest)
        if prop_ident is not None:
            prop_values, rest = _parse_prop_values(rest)
            node.properties[prop_ident] = prop_values
    if not rest:
        # Reached end of string before finding the first child node
        return node
    assert rest[0] == ';', f"Expected ';' but found {rest[:10]}..."
    index = 1
    while index < len(rest):
        child, j = _parse_node(rest[index:])
        node.children.append(child)
        index += j
    return node, index + 1

def _parse_prop_ident(input_string):
    match = re.match(r'\s*([A-Za-z]+)\s*\[', input_string)
    if not match:
        return None, input_string
    ident = match.group(1)
    length = len(ident) + 2  # account for '[' character after property identifier
    return ident, input_string[length:]

def _parse_prop_values(input_string):
    values = []
    i = 0
    while i < len(input_string):
        if input_string[i] == '\\':
            values.append(_parse_escaped_value(input_string[i+1:]))
            i += 3   # skip escaped character and backslash
        elif input_string[i] == ']':
            break
        else:
            values.extend(_parse_non_escaped_values(input_string[i:]))
            break
    return values, i + 2  # account for ']' character that ends this property

def _parse_escaped_value(input_string):
    if input_string[0] in {'t', 'T'} and len(input_string) >= 2 and input_string[1].isspace() and input_string[1] != '\n':
        return input_string[0]
    elif input_string[0] == 'n' and len(input_string) >= 2 and input_string[1] == '\n':
        return ''
    else:
        return input_string[0]

def _parse_non_escaped_values(input_string):
    values = []
    start = 0
    i = 0
    while i < len(input_string):
        if input_string[i] in {'\\', ']'}:
            values.append(input_string[start:i])
            if input_string[i] == '\\':
                i += 2  # skip over next character as well
            else:
                i += 1  # we reached the end of this property
            start = i
        else:
            i += 1
    if start < i:
        values.append(input_string[start:i])
    return [v.replace('\t', '').replace('\n', '') for v in values]
