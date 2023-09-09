def tree_from_traversals(preorder, inorder):

    if len(preorder) != len(inorder):
        raise ValueError("traversals must be the same length")

    nodes = {val: None for val in set(preorder)}

    def build_tree(preorder_left, preorder_right, inorder_left, inorder_right):
        if preorder_left > preorder_right:
            return
        
        root_val = preorder[preorder_left]
        root = nodes[root_val]

        root_index = inorder.index(root_val)

        root['l'] = build_tree(preorder_left+1, preorder_left + root_index - inorder_left, inorder_left, root_index-1)
        root['r'] = build_tree(preorder_left + root_index - inorder_left + 1, preorder_right, root_index + 1, inorder_right)

        return root

    inorder = inorder
    return build_tree(0, len(preorder)-1, 0, len(inorder)-1)
