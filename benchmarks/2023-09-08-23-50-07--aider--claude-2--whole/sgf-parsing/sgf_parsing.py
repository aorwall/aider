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
        raise ValueError("Input string is empty")
    
    nodes = []
    stack = [nodes]
    cur_node = {}

    for line in input_string.split("\n"):
        if not line.startswith("("):
            continue

        if line.endswith(")"):
            if cur_node:
                stack[-1].append(SgfTree(cur_node))
            cur_node = {}
            if stack:
                stack.pop()
            continue
        
        line = line[1:-1]
        
        if ";" in line:
            props = line.split(";")
            for prop in props:
                prop = prop.strip()
                if not prop:
                    continue
                key, value = prop.split("[")
                key = key.strip()
                value = value[:-1].replace("\\n", "\n").replace("\\]", "]")
                values = value.split("]")
                cur_node[key] = values
        else:
            if not cur_node:
                raise ValueError("Tree contains no nodes")
            stack.append(cur_node.setdefault("children", []))
    
    if not nodes:
        raise ValueError("Tree contains no nodes")

    return nodes[0]
