class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self._insert(data, node.left)
        else:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._search(data, node.left)
        else:
            return self._search(data, node.right)

    def __str__(self):
        return str(self.root)
