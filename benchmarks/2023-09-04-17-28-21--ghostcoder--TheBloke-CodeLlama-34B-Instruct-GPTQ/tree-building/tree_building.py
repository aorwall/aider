from typing import List

class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def build_tree(records: List[Record]) -> Node:
    """Build a tree from a list of records."""
    # Sort the records by their IDs
    sorted_records = sorted(records, key=lambda r: r.record_id)

    # Create a dictionary to map each record to its corresponding node
    nodes = {r.record_id: Node(r.record_id) for r in sorted_records}

    # Set up the root node
    root = nodes[sorted_records[0].record_id]

    # Iterate over the records and create the tree structure
    for record in sorted_records:
        # Find the parent node for the current record
        parent = nodes[record.parent_id]

        # Add the current node as a child of the parent node
        parent.children.append(nodes[record.record_id])

    return root


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError("broken tree")
        if ordered_id[0] != 0:
            raise ValueError("invalid")
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError("error!")
                if j.record_id < j.parent_id:
                    raise ValueError("something went wrong!")
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError("error!")
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
