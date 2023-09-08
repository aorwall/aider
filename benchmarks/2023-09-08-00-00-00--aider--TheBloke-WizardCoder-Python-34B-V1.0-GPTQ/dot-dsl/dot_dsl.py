NODE, EDGE, ATTR = range(3)

class Graph:
    def __init__(self, nodes, edges, attrs):
        self.nodes = nodes
        self.edges = edges
        self.attrs = attrs

class Node:
    def __init__(self, id, label, attrs):
        self.id = id
        self.label = label
        self.attrs = attrs

class Edge:
    def __init__(self, src, dst, label, attrs):
        self.src = src
        self.dst = dst
        self.label = label
        self.attrs = attrs
