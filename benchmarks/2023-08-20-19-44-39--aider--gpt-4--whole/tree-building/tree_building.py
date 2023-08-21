class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda r: r.record_id)
    nodes = {r.record_id: Node(r.record_id) for r in records}

    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError("Record id is invalid or out of order.")

    for r in records:
        if r.record_id < r.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        if r.record_id != 0 and r.record_id == r.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if r.record_id != 0:
            nodes[r.parent_id].children.append(nodes[r.record_id])

    return nodes[0]
