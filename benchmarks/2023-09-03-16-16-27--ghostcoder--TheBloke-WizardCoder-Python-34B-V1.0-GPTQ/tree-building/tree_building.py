class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    # Create a dictionary to store nodes by their id
    nodes = {r.record_id: Node(r.record_id) for r in records}

    # Find the root node (the one with parent_id = 0)
    try:
        root = nodes[0]
    except KeyError:
        raise ValueError("Root node not found")

    # Iterate through each record and add children to their respective parents
    for idx, rec in enumerate(records):
        if rec.record_id < 0 or rec.record_id >= len(records):
            raise ValueError("Invalid record_id")
        elif rec.parent_id > rec.record_id:
            raise ValueError("Parent id cannot be greater than record_id")
        elif rec.parent_id == rec.record_id:
            raise ValueError("A node cannot be its own parent")
        elif rec.parent_id >= len(records):
            raise ValueError("Parent id out of bounds")
        elif rec.record_id != idx:
            raise ValueError("Records should be sorted by record_id")

        try:
            nodes[rec.parent_id].children.append(nodes[rec.record_id])
        except KeyError:
            raise ValueError("Broken tree")

    return root
