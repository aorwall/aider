class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    def helper(preorder, inorder):
        if not preorder:
            return None

        root_value = preorder[0]
        root = Node(root_value)

        root_index = inorder.index(root_value)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]

        left_preorder = [val for val in preorder if val in left_inorder]
        right_preorder = [val for val in preorder if val in right_inorder]

        root.left = helper(left_preorder, left_inorder)
        root.right = helper(right_preorder, right_inorder)

        return root

    return helper(preorder, inorder)


def tree_from_traversals(preorder, inorder):
    return build_tree(preorder, inorder)