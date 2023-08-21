class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            'v': self.value,
            'l': self.left.to_dict() if self.left else {},
            'r': self.right.to_dict() if self.right else {},
        }

def tree_from_traversals(preorder, inorder):
    if not preorder and not inorder:
        return None
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    root_value = preorder[0]
    root = Node(root_value)

    inorder_index = inorder.index(root_value)
    left_inorder = inorder[:inorder_index]
    right_inorder = inorder[inorder_index + 1:]

    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]

    root.left = tree_from_traversals(left_preorder, left_inorder)
    root.right = tree_from_traversals(right_preorder, right_inorder)

    return root.to_dict()
