class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    def build_tree(preorder, inorder):
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_preorder = [val for val in preorder if val in left_inorder]
        right_preorder = [val for val in preorder if val in right_inorder]

        root.left = build_tree(left_preorder, left_inorder)
        root.right = build_tree(right_preorder, right_inorder)

        return root

    return build_tree(preorder, inorder)
