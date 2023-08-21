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

    records.sort(key=lambda x: x.record_id)
    if records[0].record_id != 0 or records[0].parent_id != 0:
        raise ValueError('The root record has not been found')

    nodes = {0: Node(0)}
    for record in records[1:]:
        nodes[record.record_id] = Node(record.record_id)
        if record.record_id <= record.parent_id or record.record_id not in nodes:
            raise ValueError('Invalid record: {}'.format(record.record_id))

        nodes[record.parent_id].children.append(nodes[record.record_id])

    return nodes[0]
