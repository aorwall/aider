from typing import List

class Record:
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id 
        self.parent_id = parent_id

class Node:
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children: List[Node] = []
        
def build_tree(records: List[Record]) -> Node:

    if not records:
        raise ValueError("No records provided")

    nodes = {}
    root = None

    # Validate records
    max_id = max(r.record_id for r in records)
    if max_id != len(records) - 1:
       raise ValueError("Record IDs are not consecutive")

    for record in records:
       if record.record_id < 0 or record.record_id >= len(records):
           raise ValueError(f"Record ID {record.record_id} is out of bounds")
       if record.parent_id < 0 or record.parent_id >= record.record_id:
           raise ValueError(f"Parent ID {record.parent_id} is invalid for record {record}")

    # Build nodes
    for record in records:
       node = Node(record.record_id)  
       nodes[record.record_id] = node

    # Assign parents    
    for record in records:
       parent_node = nodes.get(record.parent_id)
       if not parent_node:
           raise ValueError(f"No parent node for record {record}")  
       parent_node.children.append(nodes[record.record_id])

    # Find root    
    for node in nodes.values():
       if node.node_id == 0:
           root = node
           break
       if not root:
           raise ValueError("Root node not found")

    return root
