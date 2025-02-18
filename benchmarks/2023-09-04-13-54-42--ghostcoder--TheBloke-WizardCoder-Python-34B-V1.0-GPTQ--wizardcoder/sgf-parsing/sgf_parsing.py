import re
from typing import List, Dict, Tuple

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


def _parse_node(input_string: str) -> Tuple[Dict[str, str], List['SgfTree']]:
    node_properties = {}
    children = []

    # Remove leading '('
    input_string = input_string[1:]

    while input_string:

        # Check for end of node
        if input_string[0] == ')':
            break

        # Parse property
        else:
            prop_match = re.match(r'\s*(?P<prop>[A-Za-z]+)\s*\[(?P<value>.*?)\]\s*(;|(\s+(?P<next_prop>[A-Za-z]+)(?=\s+\[))|\s*\Z))', input_string)
            if not prop_match:
                raise ValueError("invalid property format")

            prop_name = prop_match.group('prop')
            prop_value = prop_match.group('value').replace("\t","").replace("\n","\\")
            next_prop = prop_match.group('next_prop')

            if prop_name in node_properties:
                raise ValueError("duplicate property name")

            node_properties[prop_name] = prop_value

            # Move to next property
            if next_prop:
                input_string = input_string[:prop_match.start()] + input_string[prop_match.end():]
            else:
                input_string = input_string[prop_match.end():].lstrip('\n')

        # Parse child node
        if input_string.startswith('('):
            child, remaining_string = _parse_node(input_string)
            children.append(child)
            input_string = remaining_string.lstrip('\n')

    # Remove trailing ')'
    input_string = input_string[1:].lstrip('\n')

    return SgfTree(node_properties, children), input_string


def parse(input_string: str) -> SgfTree:
    if not input_string.startswith('('):
        raise ValueError("missing opening parenthesis")
    elif ';' not in input_string:
        raise ValueError("missing property delimiter")
    elif '\n' in input_string and not input_string.endswith('\n'):
        raise ValueError("unexpected EOF")

    root, remaining_string = _parse_node(input_string)

    if remaining_string:
        raise ValueError("trailing text after tree")

    return root


def parse(input_string):
    pass
