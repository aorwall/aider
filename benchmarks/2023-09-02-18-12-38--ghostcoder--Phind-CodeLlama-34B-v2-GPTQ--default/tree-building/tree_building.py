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
    # Create a map of ids to Records for quicker lookups
    record_map = {r.record_id: r for r in records}

    if len(record_map) > 0:
        max_id = max(record_map.keys()) + 1

        # Validate input
        if max_id != len(record_map):
            raise ValueError('broken tree')
        if 0 not in record_map or record_map[0].parent_id != 0:
            raise ValueError('invalid')

        trees = [Node(i) for i in range(max_id)]
        for r in records:
            if r.record_id == 0:
                continue
            try:
                trees[r.record_id].children.append(trees[r.parent_id])
            except IndexError:
                raise ValueError("Parent ID out of bounds")

        return trees[0]
    else:
        return None
