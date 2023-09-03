import copy
from collections import deque
from typing import List


class NodeNotFoundException(Exception):
    """Raises exception when a node is not found."""

def find_node(tree: 'Tree', target_label: str) -> 'Tree':
    """Finds a node by its label in the given tree.
    Returns the first node with the matching label, raises NodeNotFoundException if no match is found."""
    queue = deque([tree])
    while queue:
        current_node = queue.popleft()
        if current_node.label == target_label:
            return current_node
        queue += current_node.children
    raise NodeNotFoundException(f"Node '{target_label}' not found.")


def get_paths_helper(current_node: 'Tree', target_label: str, visited: set, current_path: list, paths: List[list], acc_path: list) -> None:
    """Helper function for finding all possible paths between two nodes in a graph using DFS algorithm."""
    current_path.append(current_node)
    visited.add(current_node.label)
    if current_node.label == target_label:
        paths.append(acc_path + [current_node.label])
    else:
        for child in current_node.children:
            if child.label not in visited:
                get_paths_helper(child, target_label, visited, current_path, acc_path + [current_node.label])
    current_path.pop()
    visited.remove(current_node.label)

def get_all_paths(graph: 'Tree', start_label: str, end_label: str) -> List[List['Tree']]:
    """Returns all possible paths between two nodes in a graph."""
    start_node = find_node(graph, start_label)
    end_node = find_node(graph, end_label)
    paths = []
    visited = set()
    get_paths_helper(start_node, end_label, visited, [], [])
    return [[find_node(graph, path_label) for path_label in path] for path in paths]


def reverse_edge(parent: 'Tree', child: 'Tree') -> None:
    """Reverses the direction of an edge in the graph."""
    parent.children.remove(child)
    child.children.append(parent)

def reverse_subtree(root: 'Tree', subtree_root: 'Tree') -> None:
    """Reverses the directions of edges within a subtree rooted at subtree_root."""
    for child in subtree_root.children:
        reverse_edge(subtree_root, child)
    for grandchild in child.children:
        reverse_subtree(subtree_root, grandchild)

def reverse_direction(tree: 'Tree', start_label: str, end_label: str) -> 'Tree':
    """Reverses the direction of edges along the shortest path between start_label and end_label."""
    start_node = find_node(tree, start_label)
    end_node = find_node(tree, end_label)
    paths = get_all_paths(tree, start_label, end_label)
    min_length = float('inf')
    min_path = []
    for path in paths:
        if len(path) < min_length:
            min_length = len(path)
            min_path = path
    for i in range(len(min_path)-1):
        reverse_edge(min_path[i], min_path[i+1])
    return tree

def orient_tree(tree: 'Tree', new_root_label: str) -> 'Tree':
    """Orients the tree such that the new_root becomes the root."""
    try:
        new_root = find_node(tree, new_root_label)
    except NodeNotFoundException:
        raise ValueError("New root not found.")
    old_root = tree
    # Reverse the edge between the original root and the new root
    reverse_edge(old_root, new_root)
    # Reverse the entire subtree rooted at the new root
    reverse_subtree(new_root, new_root)
    return new_root
from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __repr__(self):
        return f"{self.label}: {','.join([c.label for c in sorted(self.children)]}"

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        """Returns the tree reoriented to center on from_node."""
        try:
            return orient_tree(copy.deepcopy(self), from_node)
        except ValueError as e:
            raise ValueError(e.args[0])

    def path_to(self, from_node, to_node):
        """Returns the path between from_node and to_node in the tree."""
        try:
            return get_all_paths(self, from_node, to_node)[0]
        except IndexError:
            raise ValueError("No path found")
