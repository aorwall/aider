import re
from typing import List, Tuple
NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        pass

def parse_graph(data: str) -> Graph:
    """Parses a string representation of a graph into a Graph object."""

    # Your implementation here
    pass

def serialize_graph(graph: Graph) -> str:
    """Serializes a Graph object into its string representation."""

    # Your implementation here
    pass
