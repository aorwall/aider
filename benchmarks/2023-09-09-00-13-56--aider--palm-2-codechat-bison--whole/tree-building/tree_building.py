class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """
    This function builds a tree from a list of records.

    Args:
        records: A list of records. Each record is a tuple of (record_id, parent_id).

    Returns:
        The root node of the tree.
    """

    if not records:
        return None

    # Sort the records by their ID numbers.
    records.sort(key=lambda x: x.record_id)

    # Check if the tree is valid.
    if records[0].parent_id != 0:
        raise ValueError('The root record must have a parent ID of 0.')
    for i in range(1, len(records)):
        if records[i].parent_id > records[i].record