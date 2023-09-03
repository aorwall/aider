class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, *args):
        for data in args:
            if self.root is None:
                self.root = TreeNode(data)
            else:
                self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)
        else:
            node.data = data

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return False

    def _find(self, data, node):
        if data == node.data:
            return True
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

        return False

    def sorted_data(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)

        return result
