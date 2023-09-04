from typing import List, Tuple

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
        self._nodes = set()
        self._edges = set()
        self._attributes = {}

        if not data:
            return

        for item in data:
            if len(item) != 2:
                raise TypeError('Invalid input')

            typ, value = item

            if typ == NODE:
                node = self._create_node(*value)
                self._add_node(node)
            elif typ == EDGE:
                edge = self._create_edge(*value)
                self._add_edge(edge)
            else:
                self._set_attribute(*value)

    @property
    def nodes(self):
        return list(self._nodes)

    @property
    def edges(self):
        return list(self._edges)

    @property
    def attributes(self):
        return dict(self._attributes)

    def _create_node(self, name, attrs):
        if not isinstance(name, str):
            raise TypeError('Name must be string')

        if not isinstance(attrs, dict):
            raise TypeError('Attrs must be dictionary')

        return Node(name, attrs)

    def _add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')

        self._nodes.add(node)

    def _create_edge(self, src, dst, attrs):
        if not isinstance(src, str):
            raise TypeError('Source must be string')

        if not isinstance(dst, str):
            raise TypeError('Destination must be string')

        if not isinstance(attrs, dict):
            raise TypeError('Attrs must be dictionary')

        return Edge(src, dst, attrs)

    def _add_edge(self, edge):
        if edge in self._edges:
            raise ValueError('Duplicate edge')

        self._edges.add(edge)

    def _set_attribute(self, key, val):
        if not isinstance(key, str):
            raise TypeError('Attribute key must be string')

        if not isinstance(val, (str, int)):
            raise TypeError('Attribute value must be string or integer')

        self._attributes[key] = val
