class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode({self.data}, {self.left}, {self.right})"


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
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)

    def data(self):
        return self.sorted_data()

    def sorted_data(self):
        result = []
        self._sort(result, self.root)
        return result

    def _sort(self, result, node):
        if node is not None:
            self._sort(result, node.left)
            result.append(node.data)
            self._sort(result, node.right)


if __name__ == "__main__":
    bst = BinarySearchTree([10, 5, 15, 8])
    print(bst.data()) # [5, 8, 10, 15]
