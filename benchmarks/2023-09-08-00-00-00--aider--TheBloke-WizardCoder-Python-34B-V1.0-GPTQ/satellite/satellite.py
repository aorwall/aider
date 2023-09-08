class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder or not inorder:
        return None

    root = preorder[0]
    root_index = inorder.index(root)

    left_preorder = preorder[1:root_index + 1]
    left_inorder = inorder[:root_index]
    left_subtree = tree_from_traversals(left_preorder, left_inorder)

    right_preorder = preorder[root_index + 1:]
    right_inorder = inorder[root_index + 1:]
    right_subtree = tree_from_traversals(right_preorder, right_inorder)

    return Node(root, left_subtree, right_subtree)
