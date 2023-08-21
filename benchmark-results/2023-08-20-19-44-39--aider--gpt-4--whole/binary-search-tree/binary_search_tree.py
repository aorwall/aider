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

    def data(self):
        return self.root

    def sorted_data(self):
        return self._in_order_traversal(self.root, [])

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def search(self, data):
        return self._search(self.root, data)

    def _insert(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def _search(self, node, data):
        if node is None:
            return None
        elif data == node.data:
            return node
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    def _in_order_traversal(self, node, sorted_data):
        if node is not None:
            self._in_order_traversal(node.left, sorted_data)
            sorted_data.append(node.data)
            self._in_order_traversal(node.right, sorted_data)
        return sorted_data
