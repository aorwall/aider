class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.insert(data)

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)

    def data(self):
        return self.root

    def sorted_data(self):
        return self._in_order_traversal(self.root, [])

    def _in_order_traversal(self, node, sorted_data):
        if node is not None:
            self._in_order_traversal(node.left, sorted_data)
            sorted_data.append(node.data)
            self._in_order_traversal(node.right, sorted_data)
        return sorted_data
