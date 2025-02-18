class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.__dict__ == other
        else:
            return super().__eq__(other)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

def tree_from_traversals(preorder, inorder):
    # Check input validity
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    set_preorder = set(preorder)
    set_inorder = set(inorder)

    if set_preorder - set_inorder or set_inorder - set_preorder:
        raise ValueError("traversals must have the same elements")

    if len(set_preorder) < len(preorder) or len(set_inorder) < len(inorder):
        raise ValueError("traversals must contain unique items")

    # Recursive function for building the tree
    def build_tree(preorder, inorder):
        if not preorder:
            return None

        root = Node(preorder[0])
        inorder_index = inorder.index(root.value)

        root.left = build_tree(preorder[1 : inorder_index + 1], inorder[:inorder_index])
        root.right = build_tree(preorder[inorder_index + 1: ], inorder[inorder_index + 1: ])

        return root

    return build_tree(preorder, inorder)
