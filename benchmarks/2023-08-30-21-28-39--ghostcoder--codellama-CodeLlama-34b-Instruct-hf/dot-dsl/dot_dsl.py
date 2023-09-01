import typing

class Graph:
    def __init__(self, data: typing.List[typing.Tuple[str, typing.Any]]):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

class Node:
    def __init__(self, name: str, attrs: typing.Dict[str, typing.Any]):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs

class Edge:
    def __init__(self, src: str, dst: str, attrs: typing.Dict[str, typing.Any]):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)

def parse_graph(data: typing.List[typing.Tuple[str, typing.Any]]) -> Graph:
    graph = Graph(data)
    for node in graph.data:
        if not isinstance(node, Node):
            raise TypeError("Graph data malformed")
    for edge in graph.data:
        if not isinstance(edge, Edge):
            raise TypeError("Graph data malformed")
    return graph

def parse_node(data: typing.Tuple[str, typing.Any]) -> Node:
    name, attrs = data
    if not isinstance(name, str):
        raise ValueError("Node name must be a string")
    if not isinstance(attrs, dict):
        raise ValueError("Node attributes must be a dictionary")
    return Node(name, attrs)

def parse_edge(data: typing.Tuple[str, str, typing.Any]) -> Edge:
    src, dst, attrs = data
    if not isinstance(src, str):
        raise ValueError("Edge source must be a string")
    if not isinstance(dst, str):
        raise ValueError("Edge destination must be a string")
    if not isinstance(attrs, dict):
        raise ValueError("Edge attributes must be a dictionary")
    return Edge(src, dst, attrs)