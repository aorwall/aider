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
        data = []
        self._traverse(self.root, data)
        return data

    def _traverse(self, node, data):
        if node is None:
            return
        self._traverse(node.left, data)
        data.append(node.data)
        self._traverse(node.right, data)

    def sorted_data(self):
        data = []
        self._in_order_traverse(self.root, data)
        return data

    def _in_order_traverse(self, node, data):
        if node is None:
            return
        self._in_order_traverse(node.left, data)
        data.append(node.data)
        self._in_order_traverse(node.right, data)
        
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(value, node.right)
        else:
            print("Value already in tree!")

    def search(self, value):
        if self.root is None:
            return False
        
        return self._search(value, self.root)
            
    def _search(self, value, node):
        if value == node.data:
            return True
        elif value < node.data and node.left is not None:
           