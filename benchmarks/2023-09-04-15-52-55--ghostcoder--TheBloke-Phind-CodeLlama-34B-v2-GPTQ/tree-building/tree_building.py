class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]

    # Check validity of the tree
    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError("Record id is invalid or out of order.")
        if ordered_id[0] != 0:
            raise ValueError("Root must start at 0")

    # Create nodes
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError("Root node should have itself as parent")
                if j.record_id < j.parent_id:
                    raise ValueError("Node parent_id should be smaller than it's record_id.")
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError("Parent node should not be a child")
                trees.append(Node(ordered_id[i]))

    # Connect parents and children
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
