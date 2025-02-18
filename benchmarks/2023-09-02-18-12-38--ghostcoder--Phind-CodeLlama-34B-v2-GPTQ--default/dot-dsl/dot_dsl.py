NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs=None):
        self.name = name
        if attrs is None:
            attrs = {}
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs=None):
        self.src = src
        self.dst = dst
        if attrs is None:
            attrs = {}
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        if data is None:
            data = []

        nodes = {}
        edges = []
        for item in data:
            itype, value = item[0], item[1]

            if itype == NODE:
                node = Node(*value)
                nodes[node.name] = node

            elif itype == EDGE:
                edge = Edge(*value)
                if edge.src not in nodes or edge.dst not in nodes:
                    raise ValueError("EDGE malformed")
                edges.append(edge)

            else: # ATTR
                pass  # handle attributes here

        if len(nodes) == 0 or len(edges) == 0:
            raise TypeError("Graph data malformed")

        self.nodes = nodes
        self.edges = edges
