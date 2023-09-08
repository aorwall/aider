class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

class BuildTree:
    def __init__(self, records):
        self.records = records

    def build_tree(self):
        root = None
        nodes = {}

        for record in self.records:
            nodes[record.record_id] = Node(record)

        for node in nodes.values():
            if node.record.parent_id == node.record.record_id:
                root = node
            else:
                nodes[node.record.parent_id].children.append(node)

        if not root:
            raise ValueError("Invalid tree input: no root found")

        return root

class Node:
    def __init__(self, record):
        self.record = record
        self.children = []

    def __repr__(self):
        return f"Node({self.record.record_id}, parent_id={self.record.parent_id})"
