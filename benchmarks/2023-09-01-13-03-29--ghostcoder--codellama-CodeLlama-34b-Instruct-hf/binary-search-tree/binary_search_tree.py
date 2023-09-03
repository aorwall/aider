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

    def search(self, data):
        if self.root is None:
            return False
        else:
            return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def sorted_data(self):
        if self.root is None:
            return []
        else:
            return self._sorted_data(self.root, [])

    def _sorted_data(self, node, data):
        if node is None:
            return data
        else:
            data.append(node.data)
            self._sorted_data(node.left, data)
            self._sorted_data(node.right, data)
            return data
