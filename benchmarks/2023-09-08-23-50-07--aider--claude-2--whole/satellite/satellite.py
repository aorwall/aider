def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
        
    preorder_set = set(preorder)
    inorder_set = set(inorder)
    if preorder_set != inorder_set:
        raise ValueError("traversals must have the same elements")
        
    if len(preorder_set) != len(preorder) or len(inorder_set) != len(inorder):
        raise ValueError("traversals must contain unique items")
        
    root = preorder[0]
    root_index = inorder.index(root)
    
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    
    left_preorder = preorder[1:len(left_inorder)+1]
    right_preorder = preorder[len(left_inorder)+1:]
    
    tree = {
        'v': root,
        'l': tree_from_traversals(left_preorder, left_inorder) if left_preorder else {},
        'r': tree_from_traversals(right_preorder, right_inorder) if right_preorder else {}
    }
    
    return tree

