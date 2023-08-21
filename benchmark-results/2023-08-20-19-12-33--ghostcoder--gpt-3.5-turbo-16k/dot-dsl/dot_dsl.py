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
            self.data = []
        else:
            self.data = data
        self.nodes = []  # Add nodes attribute

    def __eq__(self, other):
        return self.data == other.data

    def add_node(self, name, attrs=None):
        if attrs is None:
            attrs = {}
        node = Node(name, attrs)
        self.data.append((NODE, node))
        self.nodes.append(node)  # Add node to nodes attribute

    def add_edge(self, src, dst, attrs=None):
        if attrs is None:
            attrs = {}
        edge = Edge(src, dst, attrs)
        self.data.append((EDGE, edge))

    def add_attr(self, attrs):
        self.data.append((ATTR, attrs))