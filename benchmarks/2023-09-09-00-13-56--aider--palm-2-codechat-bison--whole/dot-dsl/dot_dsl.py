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
            if not isinstance(data, list):
                raise TypeError("Graph data must be a list")
            for item in data:
                if not isinstance(item, tuple):
                    raise TypeError("Graph data must be a list of tuples")
                if len(item) not in (2, 3):
                    raise TypeError("Graph data must be a list of tuples of length 2 or 3")
                if len(item) == 2:
                    if item[0] != NODE:
                        raise ValueError("First item in tuple must be NODE")
                    self.data.append(Node(item[1], {}))
                elif len(item) == 3:
                    if item[0] != EDGE:
                        raise ValueError("First item in tuple must be EDGE")
                    self.data.append(Edge(item[1], item[2], {}))
                else:
                    raise ValueError("Graph data must be a list of tuples of length 2 or 3")

    def __eq__(self, other):
        if not isinstance(other, Graph):
            return False
        return self.data == other.data

    def __str__(self):
        return "Graph({})