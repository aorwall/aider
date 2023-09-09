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
    
    if not records:
        return root
    
    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError('IDs are not sequential')
        
    if ordered_id[0] != 0:
        raise ValueError('Root node ID is not 0')
        
    trees = []
    parent = {}
    
    for i in range(len(ordered_id)):
        for record in records:
            if ordered_id[i] == record.record_id:
                
                if record.record_id == 0 and record.parent_id != 0:
                    raise ValueError('Root node parent ID is not 0')
                    
                if record.record_id < record.parent_id:
                    raise ValueError('Node parent_id should be smaller than its record_id')
                    
                if record.record_id == record.parent_id and record.record_id != 0:
                    raise ValueError('Only root should have equal record and parent id')
                    
                trees.append(Node(ordered_id[i]))
                
    for i in range(len(ordered_id)):
        for node in trees:
            if i == node.node_id:
                parent = node
                
        for record in records:
            if record.parent_id == i:
                for child in trees:
                    if child.node_id == record.record_id:
                        parent.children.append(child)
                        
    if trees:
        root = trees[0]
        
    return root
