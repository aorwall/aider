def tree_from_traversals(preorder, inorder):
    """
    Return a tree constructed from the given preorder and inorder traversals.
    
    Args:
        preorder (list[object]): A list representing the preorder traversal of the tree.
        inorder (list[object]): A list representing the inorder traversal of the tree.
    
    Returns:
        TreeNode: The root node of the constructed tree.
    """
    # Check if inputs are valid
    if len(preorder) != len(inorder):
        raise ValueError("Traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("Traversals must have the same elements")
    if len(set(preorder)) < len(preorder):
        raise ValueError("Traversals must contain unique items")

    # Construct the tree recursively
    if preorder:
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]
        root = TreeNode(root_val)
        root.left = tree_from_traversals(left_preorder, left_inorder)
        root.right = tree_from_traversals(right_preorder, right_inorder)
        return root

    # If input is empty, return None
    else:
        return None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
