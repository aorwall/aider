import collections

def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder) or set(preorder) != set(inorder):
        raise ValueError("traversals must have the same length and elements")

    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    def build_tree(preorder, inorder):
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        root.left = build_tree(left_preorder, left_inorder)
        root.right = build_tree(right_preorder, right_inorder)

        return root

    return build_tree(preorder, inorder)

def tree_to_inorder(node):
    result = []

    if node is None:
        return result

    result += tree_to_inorder(node.left)
    result.append(node.val)
    result += tree_to_inorder(node.right)

    return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

test_cases = [
    ([], []),
    (['a'], ['a']),
    (['a', 'b', 'c'], ['c', 'b', 'a']),
    (['a', 'b', 'c', 'd', 'e', 'f'], ['e', 'c', 'd', 'b', 'f', 'a'])
]

for case in test_cases:
    try:
        assert list(tree_to_inorder(tree_from_traversals(*case))) == case[1]
    except AssertionError:
        print(f"Failed on {case}")
