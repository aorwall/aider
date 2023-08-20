def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    def build_tree(preorder, inorder):
        if not preorder or not inorder:
            return None
        root = preorder[0]
        root_index = inorder.index(root)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        return {'v': root, 'l': build_tree(left_preorder, left_inorder), 'r': build_tree(right_preorder, right_inorder)} if root else {}

    return build_tree(preorder, inorder)
