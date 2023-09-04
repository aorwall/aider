class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, iterable=None):
        self.root = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = TreeNode(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = TreeNode(data)
            else:
                self._insert(data, cur_node.right)
        else:
            cur_node.data = data

    def data(self):
        return self.root.data if self.root else None

    def sorted_data(self):
        return [] if not self.root else self._inorder_traversal(self.root)

    def _inorder_traversal(self, start):
        """In-order traversal."""
        output = []
        if start:
            output = self._inorder_traversal(start.left)
            output.append(start.data)
            output = output + self._inorder_traversal(start.right)
        return output
