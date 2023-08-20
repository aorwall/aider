class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda r: r.record_id)
    nodes = {r.record_id: Node(r.record_id) for r in records}

    for i, r in enumerate(records):
        if i != r.record_id:
            raise ValueError('Record id is invalid or out of order.')
        if i == 0 and r.parent_id != 0:
            raise ValueError('Only root should have equal record and parent id.')
        if i > 0 and r.parent_id >= r.record_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        if r.record_id != 0:
            nodes[r.parent_id].children.append(nodes[r.record_id])

    return nodes[0] if records else None