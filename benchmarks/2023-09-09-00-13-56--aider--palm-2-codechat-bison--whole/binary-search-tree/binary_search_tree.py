class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None

        for data in tree_data:
            self.insert(data)

    def insert(self, data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
        else:
            self._insert(new_node, self.root)

    def _insert(self, new_node, current_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(new_node, current_node.right)

    def search(self, data):
        if self.root is None:
            return None
        else:
            return self._search(data, self.root)

    def sorted_data(self):
        if self.root is None:
            return []
        else:
            return self._sorted_data(self.root)

    def _sorted_data(self, current_node):
        if current_node is None:
            return []
        else:
            return self._sorted_data(current_node.left) + [current_node.data] + self._sorted_data(current_node.right)
