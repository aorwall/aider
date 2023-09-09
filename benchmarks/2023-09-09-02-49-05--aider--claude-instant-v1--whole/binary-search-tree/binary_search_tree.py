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
        if not self.root:
            self.root = TreeNode(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    break
            else: 
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    break

    def data(self):
        return self._traverse(self.root)

    def _traverse(self, current):
        if current:
            self._traverse(current.left)
            print(current.data)
            self._traverse(current.right)
