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
        
        if data:
            for item in data:
                if len(item) != 3:
                    raise TypeError("Graph data malformed")
                    
                kind, value, attrs = item
                
                if kind == NODE:
                    if not isinstance(value, str):
                        raise ValueError("NODE malformed")
                    self.nodes.append(Node(value, attrs))
                elif kind == EDGE:
                    if not isinstance(value, tuple) or len(value) != 2:
                        raise ValueError("EDGE malformed")
                    src, dst = value
                    self.edges.append(Edge(src, dst, attrs))
                elif kind == ATTR:
                    if not isinstance(attrs, dict):
                        raise TypeError("Graph attributes must be a dict")
                    self.attrs = attrs
                else:
                    raise ValueError(f"Invalid graph item: {item}")
