NODE, EDGE, ATTR = range(3)

class Node:
    def __init__(self, name, **kwargs):
        self.name = name
        self._attributes = kwargs

    @property
    def attributes(self):
        return self._attributes


    def __repr__(self):
        return f"{type(self).__name__}({self.name}, {self.attributes})"


    def __str__(self):
        if not self.attributes:
            return str(self.name)
        else:
            attrs = ", ".join([f"{k}={v}" for k, v in self.attributes.items()])
            return f"{self.name}[{attrs}]"


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Edge:
    def __init__(self, src, dst, **kwargs):
        self.src = src
        self.dst = dst
        self._attributes = kwargs

    @property
    def attributes(self):
        return self._attributes


    def __repr__(self):
        return f"{type(self).__name__}({self.src}, {self.dst}, {self.attributes})"


    def __str__(self):
        if not self.attributes:
            return f"{self.src} -> {self.dst}"
        else:
            attrs = ", ".join([f"{k}={v}" for k, v in self.attributes.items()])
            return f"{self.src} -> {self.dst} [{attrs}]"


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = []
        self.edges = []
        for node in nodes:
            self.add_node(node)
        for edge in edges:
            self.add_edge(edge)


    def add_node(self, node):
        assert isinstance(node, Node), "Can only add Nodes to a graph."
        self.nodes.append(node)

    def add_edge(self, edge):
        assert isinstance(edge, Edge), "Can only add Edges to a graph."
        self.edges.append(edge)

    def __repr__(self):
        lines = ["digraph G {"]
        for n in self.nodes:
            lines.append(f"\t{n};")
        for e in self.edges:
            lines.append(f"\t{e};")
        lines.append("}")
        return "\n".join(lines)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
