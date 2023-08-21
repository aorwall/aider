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
        if data is None:
            data = []
        if not isinstance(data, list):
            raise TypeError("Graph data malformed")
        self.nodes = []
        self.edges = []
        self.attrs = {}
        for item in data:
            if not isinstance(item, tuple) or len(item) < 2:
                raise TypeError("Graph item incomplete")
            kind, *args = item
            if kind == NODE:
                if len(args) != 2 or not isinstance(args[0], str) or not isinstance(args[1], dict):
                    raise ValueError("Node is malformed")
                self.nodes.append(Node(*args))
            elif kind == EDGE:
                if len(args) != 3 or not isinstance(args[0], str) or not isinstance(args[1], str) or not isinstance(args[2], dict):
                    raise ValueError("Edge is malformed")
                self.edges.append(Edge(*args))
            elif kind == ATTR:
                if len(args) != 2 or not isinstance(args[0], str) or not isinstance(args[1], str):
                    raise ValueError("Attribute is malformed")
                self.attrs[args[0]] = args[1]
            else:
                raise ValueError("Unknown data type")
