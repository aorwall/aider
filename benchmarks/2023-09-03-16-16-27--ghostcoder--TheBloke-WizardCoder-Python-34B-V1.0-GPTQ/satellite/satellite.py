class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_from_traversals(preorder, inorder):
    """Construct a binary tree from its preorder and inorder traversals"""
    # Raise exceptions if inputs are invalid
    if len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder):
        raise ValueError("Traversals must contain unique items")
    elif len(preorder) != len(inorder):
        raise ValueError("Traversals must have the same length")

    if not preorder or not inorder:
        return None
    else:preorder = [3, 2, 4, 7, 5, 8, 1, 6, 9, -1, -2]
        inorder = [4, 2, 7, 5, 2, 1, 5, 3, 8, 6, 9]
        root_val = preorder[0]

root = tree_from_traversals(preorder, inorder)
        print(root.value)   # Output: 3
        print(root.left.value)     # Output: 2
        print(root.right.value)    # Output: 1
        print(root.left.left.value)     # Output: 4
        print(root.left.right.value)    # Output: 7
        print(root.right.left.value)    # Output: 5
        print(root.right.right.value)   # Output: -1
        index = inorder.index(root_val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]
        root.left = tree_from_traversals(left_preorder, left_inorder)
        root.right = tree_from_traversals(right_preorder, right_inorder)
        return root
