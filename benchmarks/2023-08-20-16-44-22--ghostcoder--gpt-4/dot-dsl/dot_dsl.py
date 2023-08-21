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
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data is not None:
            if not isinstance(data, list) or not all(isinstance(i, tuple) for i in data):
                raise TypeError("Graph data malformed")

            for item in data:
                if len(item) < 2:
                    raise ValueError("Malformed graph descriptor")

                descriptor, *args = item

                if descriptor == NODE:
                    if len(args) != 2:
                        raise ValueError("Node is malformed")
                    name, attrs = args
                    self.nodes.append(Node(name, attrs))
                elif descriptor == EDGE:
                    if len(args) != 3:
                        raise ValueError("Edge is malformed")
                    src, dst, attrs = args
                    self.edges.append(Edge(src, dst, attrs))
                elif descriptor == ATTR:
                    if len(args) != 2:
                        raise ValueError("Attribute is malformed")
                    attr, value = args
                    self.attrs[attr] = value
                else:
                    raise ValueError("Unknown graph descriptor")