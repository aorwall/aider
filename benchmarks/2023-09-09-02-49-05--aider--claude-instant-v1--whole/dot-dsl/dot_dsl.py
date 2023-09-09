from typing import List

NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name: str, attrs: dict):
        if not isinstance(name, str):
            raise TypeError("Node name must be a string")
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src: Node, dst: Node, attrs: dict):
        if not isinstance(src, Node) or not isinstance(dst, Node):
            raise TypeError("Edge source and destination must be Node objects")
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data: List[List] = None):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []
        
        if data is None:
            data = []
            
        if not isinstance(data, list):
            raise TypeError("Graph data must be a list")
            
        for item in data:
            if len(item) != 3:
                raise ValueError("Each item in the Graph data list must contain exactly 3 elements")
                
            item_type, src_or_name, attrs = item
                
            if item_type == NODE:
                if not isinstance(src_or_name, str):
                    raise TypeError("Node name must be a string")
                if not isinstance(attrs, dict):
                    raise TypeError("Node attributes must be a dictionary")
                self.nodes.append(Node(src_or_name, attrs))
                
            elif item_type == EDGE:
                if not isinstance(src_or_name, Node) or not isinstance(attrs, dict):
                    raise TypeError("Edge source must be a Node, attributes must be a dictionary")
                self.edges.append(Edge(src_or_name, attrs))
                
            elif item_type == ATTR:
                raise NotImplementedError("Graph attributes not yet supported")
                
            else:
                raise ValueError("Item type must be NODE, EDGE or ATTR")
