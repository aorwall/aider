class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def tree_from_traversals(preorder, inorder):
    # Check for exceptions
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    node_map = {node: index for index, node in enumerate(inorder)}
    root = TreeNode(preorder[0])
    stack = [root]
    for i in range(1, len(preorder)):
        parent = stack[-1]
        node = TreeNode(preorder[i])
        if node_map[parent.val] < node_map[node.val]:
            parent.right = node
        else:
            parent.left = node
        stack.append(node)
    return root
