class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, values=[]):
        if len(values) > 0:
            for value in values:
                self.insert(value)

    def insert(self, data):
        """Insert a new value into the BST."""
        if not self.root:
            self.root = TreeNode(data)
        else:
            node = self.root
            while True:
                if data < node.data:
                    if not node.left:
                        node.left = TreeNode(data)
                        break
                    else:
                        node = node.left
                elif data > node.data:
                    if not node.right:
                        node.right = TreeNode(data)
                        break
                    else:
                        node = node.right
                else:
                    break  # Value already exists in tree

    def search(self, data):
        """Return True if `data` is present in the BST, False otherwise."""
        node = self.root
        while node:
            if data == node.data:
                return True
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def sorted_data(self):
        """Return a list of all values in the BST, sorted from smallest to largest."""
        result = []
        if self.root:
            self._sorted_data(self.root, result)
        return result

    def _sorted_data(self, node, result):
        """Helper function for sorted_data that recursively traverses the tree and appends each value to the result list."""
        if node.left:
            self._sorted_data(node.left, result)
        result.append(node.data)
        if node.right:
            self._sorted_data(node.right, result)
