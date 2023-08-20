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
            for item in data:
                if isinstance(item, tuple):
                    if len(item) == 2:
                        attr_name, attr_value = item
                        self.attrs[attr_name] = attr_value
                    elif len(item) == 3:
                        item_type, item_name, item_attrs = item
                        if item_type == NODE:
                            self.nodes.append(Node(item_name, item_attrs))
                        elif item_type == EDGE:
                            src, dst = item_name
                            self.edges.append(Edge(src, dst, item_attrs))
                        elif item_type == ATTR:  # Added this condition
                            self.attrs[item_name] = item_attrs
                        else:
                            raise ValueError("Invalid item type")
                    else:
                        raise ValueError("Invalid item format")
                else:
                    raise ValueError("Invalid item format")
