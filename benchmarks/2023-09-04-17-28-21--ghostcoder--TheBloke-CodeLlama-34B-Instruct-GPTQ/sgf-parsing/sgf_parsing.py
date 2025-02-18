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
    # Remove comments
    input_string = re.sub("\(\s*.*?\s*\)\s*$", "", input_string)

    # Split into lines
    lines = input_string.split(";")

    # Parse each line
    trees = []
    current_trees = None
    for line in lines:
        # Strip leading and trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Get the node properties
        properties = _parse_node(line)

        # Create a new tree if there aren't any current ones
        if not current_trees:
            current_trees = [SgfTree([], [])]

        # Add the node to each current tree
        next_trees = []
        for tree in current_trees:
            tree.children.append(SgfTree(properties))
            next_trees.extend(tree.children)

        # Set the current trees to the next trees
        current_trees = next_trees

    # Return the final trees
    return current_trees


def _parse_node(line):
    # Initialize the dictionary of properties
    properties = defaultdict(list)

    # Iterate over the segments in the line
    for segment in line.split("]"):
        # Check if the segment has a colon
        if ":" not in segment:
            continue

        # Extract the key and values
        key, *values = segment.split(":")

        # Add the values to the list for the key
        properties[key].extend(values)

    # Convert the lists to tuples
    properties = {k: tuple(v) for k, v in properties.items()}

    return properties
