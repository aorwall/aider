class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for data in tree_data[1:]:
            self.insert(data)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.in_order_traversal(self.root, [])

    def insert(self, data):
        node = self.root
        while node:
            if data <= node.data:
                if node.left is None:
                    node.left = TreeNode(data)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                    return
                else:
                    node = node.right

    def in_order_traversal(self, node, sorted_data):
        if node is not None:
            self.in_order_traversal(node.left, sorted_data)
            sorted_data.append(node.data)
            self.in_order_traversal(node.right, sorted_data)
        return sorted_data