def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("Traversals must have the same length")
    if len(preorder) == 0:
        return None
    root = preorder[0]
    left = tree_from_traversals(preorder[1:], inorder[:inorder.index(root)])
    right = tree_from_traversals(preorder[inorder.index(root)+1:], inorder[inorder.index(root)+1:])
    return {'v': root, 'l': left, 'r': right}
