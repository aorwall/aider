import re
from collections import defaultdict

NODE, EDGE, ATTR = range(3)


def parse_attributes(line):
    key_value_pairs = re.findall(r'(\w+)="([^"]*)"', line)
    return dict(key_value_pairs)


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
        self._nodes = []
        self._edges = []
        self._attrs = {}

        if isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    self._nodes.append(Node(item, {}))
                elif isinstance(item, tuple) and len(item) == 2:
                    self._nodes.append(Node(*item))
                elif isinstance(item, Edge):
                    self._edges.append(item)
        elif isinstance(data, str):
            lines = data.split('\n')
            lines.pop(0)  # Remove first line containing 'graph {'

            while lines:
                line = lines.pop(0).strip()

                if line == '}':
                    break

                elif line.startswith('//'):
                    continue

                elif line.endswith(';'):
                    line = line[:-1].strip()

                    if line.startswith('node'):
                        node_name, attrs = re.match(r'node\s*\[(.*)\]\s*(.*)', line).groups()
                        self._nodes.append(Node(node_name, parse_attributes(attrs)))

                    elif line.startswith('edge'):
                        edge_str = re.search(r'edge\s*\[(.*)\]\s*(.*)', line).group(2)
                        src, dst = re.match(r'\s*(.*)->(.*)\s*', edge_str).groups()
                        attrs = parse_attributes(re.sub(r'\s*(.*)->(.*)\s*', '', edge_str))
                        self._edges.append(Edge(src, dst, attrs))

                    else:
                        key, value = line.split('=')
                        self._attrs[key.strip()] = value.strip().replace('"', '')
        else:
            raise ValueError("Invalid input type")

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges

    @property
    def attributes(self):
        return self._attrs

    def __eq__(self, other):
        return (self.nodes == other.nodes and
                self.edges == other.edges and
                self.attributes == other.attributes)
