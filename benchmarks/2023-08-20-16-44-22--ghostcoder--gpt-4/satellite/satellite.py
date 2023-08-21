def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder and not inorder:
        return {}

    root = preorder[0]
    root_index = inorder.index(root)

    left_subtree = tree_from_traversals(preorder[1:root_index+1], inorder[:root_index])
    right_subtree = tree_from_traversals(preorder[root_index+1:], inorder[root_index+1:])

    return {
        'v': root,
        'l': left_subtree,
        'r': right_subtree
    }