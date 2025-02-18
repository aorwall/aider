import re
from collections import namedtuple

NodeSpec = namedtuple("NodeSpec", ["name", "attr"])
EdgeSpec = namedtuple("EdgeSpec", ["source", "destination", "attr"])
GraphSpec = namedtuple("GraphSpec", ["nodes", "edges", "attr"])

def parse_node_spec(line):
    match = re.match(r"(\w+)\[(.*?)\];$", line)
    if match:
        name, attr = match.groups()
        return NodeSpec(name, eval("dict({})".format(attr)))
    else:
        return NodeSpec(line, {})

def parse_edge_spec(line):
    match = re.match(r"(\w+) -> (\w+)(?: \[(.*?)\])?;$", line)
    if match:
        source, destination, attr = match.groups()[1:]
        return EdgeSpec(source, destination, eval("dict({})".format(attr)) if attr else {})
    else:
        raise Exception("Failed to parse edge spec")

def parse_graph_spec(lines):
    nodes = [parse_node_spec(line) for line in lines if line.endswith(";\n")]
    edges = [parse_edge_spec(line) for line in lines if line.startswith("  ")]
    return GraphSpec(nodes, edges, {})

def generate_graph_code(graph_spec):
    lines = ["{} [{}]".format(node.name, ", ".join(['='.join([k, v]) for k,v in sorted(node.attr.items())])) for node in graph_spec.nodes]
    lines += ["  {} -> {} [{}]".format(edge.source, edge.destination, ", ".join(['='.join([k, repr(v)]) for k,v in sorted(edge.attr.items())])) for edge in graph_spec.edges]
    return "\n".join(lines) + ";"

if __name__ == "__main__":
    with open("example.gv", "rt") as f:
        content = f.read().split("\n")
    graph_spec = parse_graph_spec(content)
    print(generate_graph_code(graph_spec))